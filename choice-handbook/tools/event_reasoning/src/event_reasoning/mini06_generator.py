from __future__ import annotations

from typing import Dict, List


def build_mini06(event: Dict, thesis: Dict, analogs: List[str]) -> Dict:
    return {
        "title": event.get("title", "n/a"),
        "event_id": event.get("id", "n/a"),
        "analog_list": analogs or ["n/a"],
        "tripwire": thesis.get("tripwire", "n/a"),
        "bound": thesis.get("bound", "n/a"),
        "spiral": thesis.get("spiral", "n/a"),
        "probe_48h": thesis.get("probes", {}).get("48h", "n/a"),
        "probe_7d": thesis.get("probes", {}).get("7d", "n/a"),
        "probe_30d": thesis.get("probes", {}).get("30d", "n/a"),
    }
