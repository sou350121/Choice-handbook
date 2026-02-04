from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class GateEval:
    gate: str
    evidence_score: float
    support_score: float
    counter_score: float
    rationale: str


def gate_from_confidence(confidence: float | None) -> str:
    if confidence is None:
        return "Gate 2"
    if confidence >= 0.8:
        return "Gate 3"
    if confidence >= 0.5:
        return "Gate 2"
    return "Gate 1"


def _cred_weight(credibility: str) -> float:
    c = (credibility or "").strip().lower()
    if c in {"high", "h"}:
        return 1.0
    if c in {"medium", "med", "m"}:
        return 0.6
    if c in {"low", "l"}:
        return 0.25
    # unknown → conservative
    return 0.4


def _primary_bonus(source_type: str) -> float:
    """
    Very rough heuristic: prefer primary/official texts over commentary.
    This is not meant to be perfect; it just prevents "all media" evidence
    from producing a confident Gate 3 by accident.
    """
    t = (source_type or "").strip().lower()
    primary_like = {
        "federal_register",
        "eur_lex",
        "official_gov_doc",
        "regulation_text",
        "law",
        "court_filing",
        "congressional_letter",
        "earnings_call_transcript",
        "annual_report",
        "company_annual_report",
        "financial_statement",
        "sec_filing",
        # HKEX filings are equivalent to primary market disclosures
        "hkex_pdf",
        "10k",
        "10q",
        "8k",
    }
    return 0.5 if t in primary_like else 0.0


def gate_from_evidence(
    evidence: Iterable[object],
    stated_confidence: float | None,
) -> GateEval:
    """
    Convert evidence list into a conservative gate.

    - Gate 1: weak/mostly unverified evidence
    - Gate 2: enough evidence to track / conditional action
    - Gate 3: strong primary evidence + consistency
    """
    # Note: "evidence strength" and "direction" are different.
    # If we have strong *counter evidence*, we should avoid upgrading to Gate 3.
    support_score = 0.0
    support_count = 0
    support_primary_hits = 0
    counter_score = 0.0
    counter_count = 0
    counter_primary_hits = 0
    for item in evidence:
        # duck-typing against EvidenceItem
        credibility = getattr(item, "credibility", "") or ""
        source_type = getattr(item, "source_type", "") or ""
        tags = getattr(item, "tags", []) or []
        tagset = {str(t).strip().lower() for t in (tags or []) if str(t).strip()}

        item_score = _cred_weight(str(credibility)) + _primary_bonus(str(source_type))
        is_primary = _primary_bonus(str(source_type)) > 0
        is_counter = "counter_evidence" in tagset or "counter" in tagset or "refute" in tagset or "refutes" in tagset

        if is_counter:
            counter_score += item_score
            counter_count += 1
            if is_primary:
                counter_primary_hits += 1
        else:
            support_score += item_score
            support_count += 1
            if is_primary:
                support_primary_hits += 1

    if support_count + counter_count == 0:
        # no evidence: fall back to confidence (if user provided), else Gate 1
        g = gate_from_confidence(stated_confidence) if stated_confidence is not None else "Gate 1"
        return GateEval(
            gate=g,
            evidence_score=0.0,
            support_score=0.0,
            counter_score=0.0,
            rationale="no_evidence_items; fallback_to_confidence_or_gate1",
        )

    # normalize: per-item average (support vs counter)
    support_avg = support_score / support_count if support_count else 0.0
    counter_avg = counter_score / counter_count if counter_count else 0.0
    overall_avg = (support_score + counter_score) / (support_count + counter_count)

    # conservative thresholds
    if support_avg >= 1.2 and support_primary_hits >= 1 and support_count >= 2:
        gate = "Gate 3"
        rationale = "strong_support_primary_evidence_and_consistency"
    elif support_avg >= 0.7 and support_count >= 2:
        gate = "Gate 2"
        rationale = "moderate_support_evidence; track_and_conditionals"
    else:
        gate = "Gate 1"
        rationale = "weak_or_sparse_support_evidence; avoid_action"

    # If counter evidence is also strong (esp. primary), avoid escalating to Gate 3.
    # This prevents "strong refutation" from inflating the average and producing a false Gate 3.
    if gate == "Gate 3" and counter_count >= 1 and (counter_avg >= 1.0 or counter_primary_hits >= 1):
        gate = "Gate 2"
        rationale = f"{rationale}; strong_counter_evidence_present"

    # If user provided an explicit confidence, keep it as a soft override signal:
    # - do not allow confidence to jump beyond evidence by >1 gate.
    if stated_confidence is not None:
        desired = gate_from_confidence(stated_confidence)
        order = {"Gate 1": 1, "Gate 2": 2, "Gate 3": 3}
        if order.get(desired, 2) > order.get(gate, 2) + 1:
            # e.g., confidence says Gate 3 but evidence says Gate 1 → cap at Gate 2
            gate = "Gate 2"
            rationale = f"{rationale}; capped_by_evidence_vs_confidence"
        elif order.get(desired, 2) < order.get(gate, 2) - 1:
            gate = "Gate 2"
            rationale = f"{rationale}; capped_by_confidence_vs_evidence"

    return GateEval(
        gate=gate,
        evidence_score=round(overall_avg, 3),
        support_score=round(support_avg, 3),
        counter_score=round(counter_avg, 3),
        rationale=rationale,
    )
