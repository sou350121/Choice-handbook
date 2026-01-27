from __future__ import annotations

from typing import Dict, List


def _pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.1f}%"


def render_sources_digest(run_date: str, universe: str, entries: List[Dict], delta_lines: List[str]) -> str:
    lines = [f"# {run_date} | Market Radar ({universe}) Evidence Snapshot", ""]
    lines.append("> 来源：Yahoo Finance 行情 + SEC EDGAR + 可选 RSS（仅链接，不做裁判）。")
    lines.append("")
    if delta_lines:
        lines.append("## Delta vs last run")
        lines.extend([f"- {line}" for line in delta_lines])
        lines.append("")

    lines.append("## Snapshot by ticker")
    for item in entries:
        lines.append(f"### {item['symbol']} — {item.get('name','')}")
        lines.append(f"- Tags: {', '.join(item.get('tags', [])) or 'n/a'}")
        lines.append(f"- Data source: {item.get('data_source','n/a')}")
        score = item.get("score")
        if score is not None:
            signal_tags = ", ".join(item.get("signal_tags", []) or [])
            risk_flags = ", ".join(item.get("risk_flags", []) or [])
            extra_parts = []
            if signal_tags:
                extra_parts.append(f"tags={signal_tags}")
            if risk_flags:
                extra_parts.append(f"risk={risk_flags}")
            extra = f" ({'; '.join(extra_parts)})" if extra_parts else ""
            lines.append(f"- Score: {score}{extra}")
        metrics = item.get("metrics", {})
        lines.append(
            "- Price/Change: "
            f"{metrics.get('price','n/a')} / {_pct(metrics.get('change_percent'))}"
        )
        lines.append(
            "- 5d/20d return: "
            f"{_pct(metrics.get('ret_5d'))} / {_pct(metrics.get('ret_20d'))}"
        )
        vol_avg = metrics.get("vol_avg20")
        if vol_avg:
            volume = metrics.get("volume")
            ratio = volume / vol_avg if volume else None
            lines.append(
                f"- Volume: {volume} (avg20={int(vol_avg)}) ratio={ratio:.2f}"
            )
        else:
            lines.append("- Volume: n/a")

        text_hits = item.get("text_hits", {})
        if text_hits:
            lines.append(
                "- Text hits: "
                f"supplychain={text_hits.get('supplychain', 0)}, "
                f"platform={text_hits.get('platform', 0)}, "
                f"financial={text_hits.get('financial', 0)}"
            )

        filings = item.get("filings", [])
        if filings:
            lines.append("- Recent SEC filings:")
            for filing in filings:
                desc = filing.get("description", "").strip()
                desc_part = f" {desc}" if desc else ""
                lines.append(
                    f"  - {filing['date']} {filing['form']}:{desc_part} {filing['url']}"
                )
        rss_items = item.get("rss", [])
        if rss_items:
            lines.append("- RSS headlines:")
            for rss in rss_items:
                title = rss.get("title", "")
                link = rss.get("link", "")
                lines.append(f"  - {title} — {link}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def _render_case_atlas_legend() -> List[str]:
    return [
        "**Case Atlas 编号说明**：",
        "- **11.x** = 金融危机类比（流动性/对手方/再融资风险）",
        "- **12.x** = 平台战争类比（分发/生态/规则变化）",
        "- **13.x** = 供应链与制造类比（交付/质量/单点断供）",
        "- 详见：`world_understanding/yearbook/case_atlas_financial_crisis_06.md` / "
        "`world_understanding/yearbook/case_atlas_platform_wars_06.md` / "
        "`world_understanding/yearbook/case_atlas_supply_chain_manufacturing_06.md`",
        "",
    ]


def _render_top_section(title: str, top_list: List[Dict]) -> List[str]:
    lines = [f"## {title}", ""]
    if not top_list:
        lines.append("- n/a")
        lines.append("")
        return lines
    for item in top_list:
        lines.append(f"### {item['symbol']} — {item.get('name','')}")
        analogs = " + ".join([f"{a[0]} ({a[1]})" for a in item["mini06"]["analogs"]])
        lines.append(f"- T0-Analog (Case Atlas): {analogs}")
        lines.append(f"- First Tripwire: {item['mini06']['tripwire']}")
        lines.append(f"- Catastrophic Bound: {item['mini06']['bound']}")
        lines.append(f"- Death Spiral: {item['mini06']['spiral']}")
        lines.append(f"- 最短探针: {item['mini06']['probe']}")
        lines.append("")
    return lines


def render_mini06_report(
    run_date: str,
    universe: str,
    top3_us: List[Dict],
    top3_cn: List[Dict],
    sources_path: str,
) -> str:
    lines = [f"# {run_date} | Market Radar ({universe}) Top-3 mini-06", ""]
    lines.append(f"> Evidence: `{sources_path}`")
    lines.append("")
    lines.extend(_render_case_atlas_legend())
    lines.extend(_render_top_section("Top-3 US", top3_us))
    lines.extend(_render_top_section("Top-3 HK/SH/SZ", top3_cn))
    return "\n".join(lines).strip() + "\n"


def render_rolling_summary(
    run_date: str,
    universe: str,
    sources_path: str,
    mini06_path: str,
    top3_us: List[Dict],
    top3_cn: List[Dict],
) -> str:
    lines = [f"# Market Radar — {universe} (Rolling)", ""]
    lines.append(f"- Latest run: {run_date}")
    lines.append(f"- Evidence snapshot: `{sources_path}`")
    lines.append(f"- Top-3 mini-06: `{mini06_path}`")
    lines.append("")
    lines.extend(_render_case_atlas_legend())
    lines.append("## This run: Top signals (US)")
    if not top3_us:
        lines.append("- n/a")
    else:
        for item in top3_us:
            score = item.get("score")
            bucket = item.get("mini06", {}).get("primary_bucket")
            bucket_part = f", bucket={bucket}" if bucket else ""
            lines.append(f"- {item['symbol']} — {item.get('name','')} (score={score}{bucket_part})")
    lines.append("")
    lines.append("## This run: Top signals (HK/SH/SZ)")
    if not top3_cn:
        lines.append("- n/a")
    else:
        for item in top3_cn:
            score = item.get("score")
            bucket = item.get("mini06", {}).get("primary_bucket")
            bucket_part = f", bucket={bucket}" if bucket else ""
            lines.append(f"- {item['symbol']} — {item.get('name','')} (score={score}{bucket_part})")
    lines.append("")
    lines.append("## How to use")
    lines.append(
        "- Pick 1–2 tickers, open the mini-06, and translate Tripwire/Bound/Spiral into your current decision."
    )
    lines.append("")
    return "\n".join(lines).strip() + "\n"
