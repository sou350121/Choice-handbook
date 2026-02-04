from __future__ import annotations

from pathlib import Path
from typing import List


DEFAULT_COUNTERS = {
    "regulatory": [
        "enforcement_delayed_or_narrowed",
        "scope_limited_to_specific_use_cases",
        "compliance_mitigation_reduces_impact",
    ],
    "geopolitics": [
        "carve_outs_or_licenses",
        "third_country_reroute",
        "demand_shift_to_alternative_markets",
    ],
    "supply_chain": [
        "second_source_qualified",
        "inventory_buffer_absorbs_shock",
        "demand_softening_offsets_shortage",
    ],
    "macro_policy": [
        "policy_reversal_or_soft_landing",
        "market_priced_in",
        "transmission_lag_longer_than_expected",
    ],
    "tech_breakthrough": [
        "reproducibility_failure",
        "cost_curve_not_improving",
        "integration_blockers",
    ],
    "fraud_or_misreporting": [
        "allegations_unsubstantiated",
        "impact_limited_to_subsidiary",
        "remediation_and_controls_strengthened",
    ],
}


def _load_config_counters() -> dict[str, list[str]]:
    """
    Optional: load counter paths from config/event_types.yaml.
    This makes counter hypotheses extensible without touching code.
    """
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    try:
        tool_root = Path(__file__).resolve().parents[2]  # .../tools/event_reasoning
        config_path = tool_root / "config" / "event_types.yaml"
        if not config_path.exists():
            return {}
        payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        event_types = (payload.get("event_types") or {}) if isinstance(payload, dict) else {}
        counters: dict[str, list[str]] = {}
        for k, v in event_types.items():
            if not isinstance(k, str) or not isinstance(v, dict):
                continue
            cp = v.get("counter_paths")
            if isinstance(cp, list) and all(isinstance(x, str) and x.strip() for x in cp):
                counters[k] = [x.strip() for x in cp]
        return counters
    except Exception:
        return {}


CONFIG_COUNTERS = _load_config_counters()


def derive_counter_hypotheses(event_type: str, provided: List[str] | None) -> List[str]:
    if provided:
        return provided
    if event_type in CONFIG_COUNTERS:
        return CONFIG_COUNTERS[event_type]
    return DEFAULT_COUNTERS.get(event_type, ["insufficient_evidence", "impact_overstated", "timing_mismatch"])
