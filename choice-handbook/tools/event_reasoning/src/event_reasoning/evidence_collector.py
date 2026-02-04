from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Dict, Any


@dataclass
class EvidenceItem:
    time: str
    source_type: str
    url: str
    claim: str
    quote_or_fact: str
    credibility: str
    verifiability: str
    tags: List[str]


def _normalize_str(value: Any, default: str = "n/a") -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text if text else default


def _normalize_tags(value: Any) -> List[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [str(value).strip()]


def normalize_evidence(items: Iterable[Dict[str, Any]]) -> List[EvidenceItem]:
    normalized: List[EvidenceItem] = []
    for raw in items:
        normalized.append(
            EvidenceItem(
                time=_normalize_str(raw.get("time")),
                source_type=_normalize_str(raw.get("source_type")),
                url=_normalize_str(raw.get("url")),
                claim=_normalize_str(raw.get("claim")),
                quote_or_fact=_normalize_str(raw.get("quote_or_fact")),
                credibility=_normalize_str(raw.get("credibility"), "medium"),
                verifiability=_normalize_str(raw.get("verifiability")),
                tags=_normalize_tags(raw.get("tags")),
            )
        )
    # Sort by time string if possible; keep stable order otherwise.
    normalized.sort(key=lambda item: item.time)
    return normalized


def collect_sources(evidence: Iterable[EvidenceItem]) -> List[str]:
    sources: List[str] = []
    seen = set()
    for item in evidence:
        if item.url and item.url not in seen:
            sources.append(item.url)
            seen.add(item.url)
    return sources
