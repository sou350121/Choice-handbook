from __future__ import annotations

from typing import Dict, List, Tuple

SUPPLYCHAIN_KEYWORDS = [
    "hbm",
    "nand",
    "dram",
    "memory",
    "capacity",
    "lead time",
    "datacenter",
    "data center",
    "cooling",
    "power",
    "wafer",
    "foundry",
    "packaging",
]

PLATFORM_KEYWORDS = [
    "platform",
    "app store",
    "api",
    "license",
    "open source",
    "fork",
    "distribution",
    "default",
    "bundle",
]

FINANCIAL_KEYWORDS = [
    "liquidity",
    "refinancing",
    "debt",
    "covenant",
    "default",
    "downgrade",
    "margin",
    "bankruptcy",
]


def count_keywords(text: str, keywords: List[str]) -> int:
    text_lower = text.lower()
    return sum(1 for word in keywords if word in text_lower)


def compute_metrics(quote: Dict, history: List[Dict]) -> Dict:
    metrics = {
        "price": quote.get("price"),
        "change_percent": quote.get("changesPercentage"),
        "volume": quote.get("volume"),
        "ret_1d": quote.get("changesPercentage"),
        "ret_5d": None,
        "ret_20d": None,
        "vol_avg20": None,
    }
    if not history:
        return metrics

    closes = [h.get("close") for h in history if h.get("close") is not None]
    volumes = [h.get("volume") for h in history if h.get("volume") is not None]
    if len(closes) >= 6:
        metrics["ret_5d"] = (closes[0] / closes[5]) - 1
    if len(closes) >= 21:
        metrics["ret_20d"] = (closes[0] / closes[20]) - 1
    if len(volumes) >= 20:
        metrics["vol_avg20"] = sum(volumes[:20]) / 20
    return metrics


def score_signals(metrics: Dict, text_hits: Dict[str, int]) -> Tuple[int, List[str], List[str]]:
    score = 0
    tags: List[str] = []
    risk_flags: List[str] = []

    ret_1d = metrics.get("ret_1d")
    ret_5d = metrics.get("ret_5d")
    ret_20d = metrics.get("ret_20d")
    volume = metrics.get("volume")
    vol_avg20 = metrics.get("vol_avg20")

    if ret_1d is not None and ret_5d is None and ret_20d is None:
        if ret_1d > 0.08:
            score += 2
            tags.append("momentum_1d")
        elif ret_1d < -0.08:
            risk_flags.append("drawdown_1d")

    if ret_5d is not None:
        if ret_5d > 0.3:
            score += 3
            tags.append("momentum_5d")
        elif ret_5d > 0.15:
            score += 2
            tags.append("momentum_5d")
        elif ret_5d < -0.2:
            risk_flags.append("drawdown_5d")

    if ret_20d is not None:
        if ret_20d > 0.6:
            score += 3
            tags.append("momentum_20d")
        elif ret_20d > 0.3:
            score += 2
            tags.append("momentum_20d")
        elif ret_20d < -0.3:
            risk_flags.append("drawdown_20d")

    if volume is not None and vol_avg20:
        spike = volume / vol_avg20 if vol_avg20 else 1
        if spike > 3:
            score += 3
            tags.append("volume_spike")
        elif spike > 2:
            score += 2
            tags.append("volume_spike")

    keyword_score = min(3, text_hits.get("supplychain", 0) + text_hits.get("platform", 0) + text_hits.get("financial", 0))
    score += keyword_score
    if text_hits.get("supplychain", 0) > 0:
        tags.append("keyword_supplychain")
    if text_hits.get("platform", 0) > 0:
        tags.append("keyword_platform")
    if text_hits.get("financial", 0) > 0:
        tags.append("keyword_financial")

    return score, tags, risk_flags
