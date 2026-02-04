from __future__ import annotations

from typing import List, Dict, Any

from .evidence_collector import EvidenceItem


def build_timeline(evidence: List[EvidenceItem], explicit: List[Dict[str, Any]] | None = None) -> List[Dict[str, str]]:
    if explicit:
        return [
            {
                "time": str(item.get("time", "n/a")).strip() or "n/a",
                "event": str(item.get("event", "n/a")).strip() or "n/a",
                "actors": str(item.get("actors", "")).strip(),
                "mechanism_link": str(item.get("mechanism_link", "")).strip(),
            }
            for item in explicit
        ]

    timeline: List[Dict[str, str]] = []
    for item in evidence:
        timeline.append(
            {
                "time": item.time,
                "event": item.claim,
                "actors": "",
                "mechanism_link": "",
            }
        )
    return timeline
