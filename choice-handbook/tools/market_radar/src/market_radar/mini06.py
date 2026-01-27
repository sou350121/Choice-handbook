from __future__ import annotations

from typing import Dict, List, Tuple

ANALOGS = {
    "financial": [
        ("11.14", "Dash for Cash"),
        ("11.11", "LDI 保证金螺旋"),
        ("11.17", "Evergrande 再融资墙"),
        ("11.1", "Lehman 短融断裂"),
    ],
    "platform": [
        ("12.4", "MS vs Netscape"),
        ("12.12", "Apple vs Epic"),
        ("12.14", "Teams vs Zoom"),
        ("12.15", "Elastic vs OpenSearch"),
    ],
    "supplychain": [
        ("13.12", "汽车芯片短缺"),
        ("13.1", "Toyota JIT"),
        ("13.16", "认证材料单点"),
        ("13.10", "Takata 召回扩散"),
    ],
}

TEMPLATES = {
    "financial": {
        "tripwire": "融资期限缩短/利差走阔/保证金上调出现时（参照 {primary}）",
        "bound": "融资窗关闭或赎回闸门被触发（参照 {primary}）",
        "spiral": "融资收紧 → 抛售 → 价格下跌 → 更多保证金 → 挤兑（参照 {primary}）",
        "probe": "48h：测算 haircuts 上调与波动翻倍时的现金缺口与可抵押资产。",
    },
    "platform": {
        "tripwire": "平台规则/抽成/默认入口变化开始影响单位经济学（参照 {primary}）",
        "bound": "分发被切断（下架/API关门/默认入口切断）（参照 {primary}）",
        "spiral": "规则收紧 → 单位经济学恶化 → 用户/生态流失 → 更难新增（参照 {primary}）",
        "probe": "7d：列出平台依赖度与分发地图；若规则变更，新增会掉多少？",
    },
    "memory": {
        # NOTE: We keep this as a template, but will also embed current metric values when available.
        "tripwire": "内存/显存链条进入紧约束：价格/交期/抢货开始同步抬升（参照 {primary}）",
        "bound": "合同价上调与抢货常态化，替代/扩产周期无法在 1–2 季度内缓解（参照 {primary}）",
        "spiral": "供给紧 → 现货涨 → 合同价跟涨 → 客户抢货/囤货 → 更紧（价格螺旋）（参照 {primary}）",
        "probe": "7d：做“HBM/DRAM 信号板”：价格/交期、capex/bit growth、客户指引三件套，写停机阈值。",
    },
    "supplychain": {
        "tripwire": "交期持续拉长/关键件单点/良率或缺陷率上升（参照 {primary}）",
        "bound": "关键件断供或认证替代周期>3–6个月（参照 {primary}）",
        "spiral": "缺件 → 停产 → 现金流恶化 → 更难锁产能 → 更缺件（参照 {primary}）",
        "probe": "7d：Top20关键件二供审计 + 库存覆盖天数 + 替代周期。",
    },
}


def _stable_index(symbol: str, size: int) -> int:
    return sum(ord(ch) for ch in symbol.upper()) % size


def choose_primary_bucket(watchlist_tags: List[str], text_hits: Dict[str, int], risk_flags: List[str]) -> str:
    tag_set = {t.lower() for t in watchlist_tags}
    # Memory is a special case of supply-chain, but we want tighter Tripwire wording.
    if any(t in tag_set for t in ["memory", "dram", "nand"]) or text_hits.get("supplychain", 0) > 0 and any(
        k in tag_set for k in ["gpu", "server", "compute"]
    ):
        return "memory"
    if text_hits.get("platform", 0) > 0:
        return "platform"
    if text_hits.get("financial", 0) > 0 or any("drawdown" in f for f in risk_flags):
        return "financial"
    if any(t in tag_set for t in ["memory", "dram", "nand", "power", "cooling", "server", "foundry", "capacity"]):
        return "supplychain"
    return "supplychain"


def pick_secondary(primary: str) -> str:
    if primary == "financial":
        return "supplychain"
    if primary == "platform":
        return "supplychain"
    if primary == "memory":
        return "financial"
    return "financial"


def select_analogs(symbol: str, primary: str, secondary: str) -> Tuple[Tuple[str, str], Tuple[str, str]]:
    # `memory` reuses supply-chain analog pool.
    primary_key = "supplychain" if primary == "memory" else primary
    primary_list = ANALOGS[primary_key]
    secondary_list = ANALOGS[secondary]
    p_idx = _stable_index(symbol, len(primary_list))
    s_idx = _stable_index(symbol + secondary, len(secondary_list))
    return primary_list[p_idx], secondary_list[s_idx]


def build_mini06(candidate: Dict) -> Dict:
    symbol = candidate["symbol"]
    watchlist_tags = candidate.get("tags", [])
    text_hits = candidate.get("text_hits", {})
    risk_flags = candidate.get("risk_flags", [])
    metrics = candidate.get("metrics", {}) or {}

    primary = choose_primary_bucket(watchlist_tags, text_hits, risk_flags)
    secondary = pick_secondary(primary)
    primary_analog, secondary_analog = select_analogs(symbol, primary, secondary)

    template = TEMPLATES[primary]

    def _pct(v: float | None) -> str:
        if v is None:
            return "n/a"
        return f"{v*100:.1f}%"

    def _vol_ratio() -> float | None:
        vol = metrics.get("volume")
        avg = metrics.get("vol_avg20")
        if vol is None or not avg:
            return None
        try:
            return float(vol) / float(avg)
        except Exception:
            return None

    def _metric_prefix() -> str:
        r5 = metrics.get("ret_5d")
        r20 = metrics.get("ret_20d")
        vr = _vol_ratio()
        if r5 is None and r20 is None and vr is None:
            return ""
        parts = [f"5d={_pct(r5)}", f"20d={_pct(r20)}"]
        if vr is not None:
            parts.append(f"vol_ratio={vr:.2f}")
        return "（价格/量能代理：" + ", ".join(parts) + "）"

    def _memory_tripwire() -> str:
        r5 = metrics.get("ret_5d")
        r20 = metrics.get("ret_20d")
        vr = _vol_ratio()
        parts = [
            "内存/显存链条进入紧约束：",
            "5d>15% 或 20d>30%，且 volume/avg20>2（作为“价格+关注度”代理）",
            f"当前：5d={_pct(r5)}, 20d={_pct(r20)}, vol_ratio={vr:.2f}" if vr is not None else f"当前：5d={_pct(r5)}, 20d={_pct(r20)}",
            f"（参照 {primary_analog[0]}）",
        ]
        return " ".join(parts).strip()

    def _wrap_tripwire(base: str) -> str:
        prefix = _metric_prefix()
        return f"{prefix} {base}".strip() if prefix else base

    mini06 = {
        "symbol": symbol,
        "name": candidate.get("name", ""),
        "primary_bucket": primary,
        "analogs": [primary_analog, secondary_analog],
        "tripwire": (
            _memory_tripwire()
            if primary == "memory"
            else _wrap_tripwire(template["tripwire"].format(primary=primary_analog[0]))
        ),
        "bound": template["bound"].format(primary=primary_analog[0]),
        "spiral": template["spiral"].format(primary=primary_analog[0]),
        "probe": template["probe"],
    }
    return mini06
