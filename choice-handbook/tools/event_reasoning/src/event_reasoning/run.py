from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Dict, Any, List

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[1]))

from event_reasoning.counter_evidence_checker import derive_counter_hypotheses
from event_reasoning.evidence_collector import normalize_evidence, collect_sources
from event_reasoning.gate_evaluator import gate_from_confidence, gate_from_evidence
from event_reasoning.mini06_generator import build_mini06
from event_reasoning.timeline_builder import build_timeline
from event_reasoning.writeback import update_hypotheses_registry, upsert_opportunity_block


def _load_input(path: Path) -> Dict[str, Any]:
    if path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except Exception as exc:
            raise RuntimeError("PyYAML is required for YAML input. Use JSON or install pyyaml.") from exc
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return json.loads(path.read_text(encoding="utf-8"))


def _output_date(event: Dict[str, Any]) -> str:
    raw = event.get("date")
    if raw:
        return str(raw)
    return date.today().isoformat()


def _render_sources_digest(
    event: Dict[str, Any],
    evidence_rows: List[Dict[str, str]],
    sources: List[str],
    uncertainties: List[str],
) -> str:
    title = event.get("title", "n/a")
    event_id = event.get("id", "n/a")
    scope = event.get("scope", "n/a")
    market = event.get("market", "n/a")
    lines: List[str] = []
    lines.append(f"# Event Reasoning Evidence Digest: {title}")
    lines.append("")
    lines.append(f"> Event ID: `{event_id}`  ")
    lines.append(f"> Scope: {scope}  ")
    lines.append(f"> Market: {market}")
    lines.append("")
    lines.append("## Evidence Sources (links)")
    for link in sources:
        lines.append(f"- {link}")
    lines.append("")
    lines.append("## Evidence Table")
    lines.append("")
    lines.append("| time | source_type | claim | quote_or_fact | credibility | verifiability | url |")
    lines.append("|---|---|---|---|---|---|---|")
    for row in evidence_rows:
        lines.append(
            "| {time} | {source_type} | {claim} | {quote_or_fact} | {credibility} | {verifiability} | {url} |".format(
                **row
            )
        )
    if uncertainties:
        lines.append("")
        lines.append("## Uncertainties / Blind Spots")
        lines.append("")
        for item in uncertainties:
            lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def _render_mini06_report(
    output_date: str,
    event: Dict[str, Any],
    thesis: Dict[str, Any],
    analogs: List[str],
    mini06: Dict[str, Any],
    evidence_path: str,
    timeline: List[Dict[str, str]],
    counter_hypotheses: List[str],
    gate: str,
) -> str:
    title = event.get("title", "n/a")
    summary = thesis.get("main_thesis", "n/a")
    lines: List[str] = []
    lines.append(f"# {output_date} | Event Reasoning mini-06 | {title}")
    lines.append("")
    lines.append(f"> Evidence: `{evidence_path}`")
    lines.append("")
    lines.append("## Event Summary")
    lines.append("")
    lines.append(f"- {summary}")
    lines.append(f"- Gate: **{gate}**")
    lines.append("")
    lines.append("## T0-Analog (Case Atlas)")
    lines.append("")
    if analogs:
        for item in analogs:
            lines.append(f"- {item}")
    else:
        lines.append("- n/a")
    lines.append("")
    lines.append("## Timeline (key nodes)")
    lines.append("")
    for node in timeline:
        lines.append(f"- {node['time']}: {node['event']}")
    lines.append("")
    lines.append("## Counter Hypotheses (3)")
    lines.append("")
    for idx, item in enumerate(counter_hypotheses[:3], start=1):
        lines.append(f"{idx}) {item}")
    lines.append("")
    lines.append("## Tripwire / Bound / Spiral")
    lines.append("")
    lines.append(f"- First Tripwire: {mini06['tripwire']}")
    lines.append(f"- Catastrophic Bound: {mini06['bound']}")
    lines.append(f"- Death Spiral: {mini06['spiral']}")
    lines.append("")
    lines.append("## 最短探针")
    lines.append("")
    lines.append(f"- 48h: {mini06['probe_48h']}")
    lines.append(f"- 7d: {mini06['probe_7d']}")
    lines.append(f"- 30d: {mini06['probe_30d']}")
    lines.append("")
    return "\n".join(lines)


def _render_ic_memo(
    output_date: str,
    event: Dict[str, Any],
    thesis: Dict[str, Any],
    gate: str,
    evidence_path: str,
    evidence_score: float | None,
    support_score: float | None,
    counter_score: float | None,
    gate_rationale: str | None,
) -> str:
    """
    A human-first 1-page memo.

    Goal: make the "so what / what to do / when to stop" obvious,
    while still linking to auditable evidence.
    """
    title = event.get("title", "n/a")
    event_id = event.get("id", "n/a")
    scope = event.get("scope", "n/a")
    market = event.get("market", "n/a")
    event_type = event.get("event_type", "n/a")

    main_thesis = thesis.get("main_thesis", "n/a")
    killer_assumptions = thesis.get("killer_assumptions", []) or []
    tripwire = thesis.get("tripwire", "n/a")
    bound = thesis.get("bound", "n/a")
    spiral = thesis.get("spiral", "n/a")

    market_map = thesis.get("market_map", {}) or {}
    winners = market_map.get("winners", []) or []
    losers = market_map.get("losers", []) or []
    channels = market_map.get("channels", []) or []
    watch = market_map.get("watchlist", []) or []

    scenarios = thesis.get("scenarios", []) or []
    action = thesis.get("action", {}) or {}

    lines: List[str] = []
    lines.append(f"# {output_date} | IC Memo | {title}")
    lines.append("")
    lines.append(f"> Event ID: `{event_id}`  ")
    lines.append(f"> Type: {event_type}  ")
    lines.append(f"> Scope: {scope}  ")
    lines.append(f"> Market: {market}  ")
    lines.append(f"> Gate: **{gate}**")
    if evidence_score is not None:
        lines.append(f"> Evidence score (avg): {evidence_score}")
    if support_score is not None:
        lines.append(f"> Support evidence score (avg): {support_score}")
    if counter_score is not None:
        lines.append(f"> Counter evidence score (avg): {counter_score}")
    if gate_rationale:
        lines.append(f"> Gate rationale: {gate_rationale}")
    lines.append(f"> Evidence: `{evidence_path}`")
    lines.append("")

    lines.append("## 01 结论（人话 3 句）")
    lines.append("")
    lines.append(f"- **发生了什么**：{title}")
    lines.append(f"- **核心判断**：{main_thesis}")
    lines.append(f"- **行动含义**：Gate={gate}；优先做“跟踪 + 条件动作”，并提前写好停机点（Tripwire/Bound）")
    lines.append("")

    lines.append("## 02 机制与市场传导（你该盯什么变量）")
    lines.append("")
    if channels:
        lines.append("**传导链（简版）**")
        for c in channels:
            lines.append(f"- {c}")
    else:
        lines.append("- n/a（建议在输入里补 `thesis.market_map.channels`，用箭头写传导链）")
    lines.append("")
    if winners or losers:
        if winners:
            lines.append("**潜在受益方**")
            for w in winners:
                lines.append(f"- {w}")
        if losers:
            lines.append("")
            lines.append("**潜在受损方**")
            for l in losers:
                lines.append(f"- {l}")
        lines.append("")
    if watch:
        lines.append("**观察名单（最小集合）**")
        for x in watch:
            lines.append(f"- {x}")
        lines.append("")

    lines.append("## 03 情景推演（带概率）")
    lines.append("")
    if scenarios:
        for idx, s in enumerate(scenarios, start=1):
            name = s.get("name", f"Scenario {idx}")
            p = s.get("probability", "n/a")
            tw = s.get("time_window", "n/a")
            desc = s.get("description", "n/a")
            impact = s.get("impact", "n/a")
            cond = s.get("conditions", "n/a")
            observables = s.get("observables") or s.get("observable_indicators") or []
            lines.append(f"**{idx}) {name}**")
            lines.append(f"- 概率: {p} | 时间窗: {tw}")
            lines.append(f"- 发生条件: {cond}")
            lines.append(f"- 事件展开: {desc}")
            lines.append(f"- 市场影响: {impact}")
            if isinstance(observables, list) and observables:
                lines.append("- 可观测指标（确认进入该分支）:")
                for o in observables:
                    if str(o).strip():
                        lines.append(f"  - {str(o).strip()}")
            lines.append("")
    else:
        lines.append("- n/a（建议在输入里补 `thesis.scenarios`，至少 3 个情景：base/bull/bear）")
        lines.append("")

    lines.append("## 04 行动方案（默认动作 + 条件动作）")
    lines.append("")
    default_action = action.get("default", "n/a")
    if_tripwire = action.get("if_tripwire", "n/a")
    if_bound = action.get("if_bound", "n/a")
    hedges = action.get("hedges", []) or []
    lines.append(f"- **默认动作**: {default_action}")
    lines.append(f"- **触发 Tripwire 后**: {if_tripwire}")
    lines.append(f"- **触发 Bound 后（止损/撤退）**: {if_bound}")
    if hedges:
        lines.append("- **对冲/保险**:")
        for h in hedges:
            if isinstance(h, dict) and h:
                k = next(iter(h.keys()))
                lines.append(f"  - {k}: {h[k]}")
            else:
                lines.append(f"  - {h}")
    lines.append("")

    lines.append("## 05 风险与停机点（这部分决定你会不会亏大钱）")
    lines.append("")
    if killer_assumptions:
        lines.append("**Killer assumptions（被打脸就要退）**")
        for ka in killer_assumptions:
            lines.append(f"- {ka}")
        lines.append("")
    lines.append(f"- **Tripwire（第一次警报）**: {tripwire}")
    lines.append(f"- **Bound（硬红线）**: {bound}")
    lines.append(f"- **Spiral（负反馈螺旋）**: {spiral}")
    lines.append("")

    lines.append("## 06 下一步最小探针（48h/7d/30d）")
    lines.append("")
    probes = thesis.get("probes", {}) or {}
    lines.append(f"- 48h: {probes.get('48h', 'n/a')}")
    lines.append(f"- 7d: {probes.get('7d', 'n/a')}")
    lines.append(f"- 30d: {probes.get('30d', 'n/a')}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Event reasoning runner (MVP).")
    parser.add_argument("--input", required=True, help="Path to event YAML/JSON input.")
    parser.add_argument("--writeback", action="store_true", help="Enable optional writeback to meta/distilled.")
    parser.add_argument("--hypothesis-id", help="Existing H-XXXX to append evidence to.")
    parser.add_argument("--opportunity-title", help="Title to insert into opportunity_map.md.")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    payload = _load_input(input_path)

    event = payload.get("event", {}) or {}
    thesis = payload.get("thesis", {}) or {}
    evidence_raw = payload.get("evidence", []) or []
    timeline_raw = payload.get("timeline")
    uncertainties = payload.get("uncertainties", []) or []

    evidence_items = normalize_evidence(evidence_raw)
    sources = collect_sources(evidence_items)
    timeline = build_timeline(evidence_items, timeline_raw)

    event_type = event.get("event_type", "regulatory")
    counter_hypotheses = derive_counter_hypotheses(event_type, thesis.get("counter_hypotheses"))

    confidence = thesis.get("confidence")
    gate_eval = gate_from_evidence(evidence_items, confidence)
    gate = thesis.get("gate") or gate_eval.gate or gate_from_confidence(confidence)

    output_date = _output_date(event)
    event_id = event.get("id", "event")
    evidence_filename = f"{output_date}_event_reasoning_{event_id}.md"
    mini06_filename = f"{output_date}_{event_id}_mini06.md"
    memo_filename = f"{output_date}_{event_id}_memo.md"

    repo_root = Path(__file__).resolve().parents[4]
    sources_dir = repo_root / "sources"
    runs_dir = repo_root / "world_understanding" / "event_reasoning_runs"

    evidence_path = sources_dir / evidence_filename
    mini06_path = runs_dir / mini06_filename
    memo_path = runs_dir / memo_filename

    analogs = event.get("analogs", []) or []
    mini06 = build_mini06(event, thesis, analogs)

    evidence_rows = [
        {
            "time": item.time,
            "source_type": item.source_type,
            "claim": item.claim,
            "quote_or_fact": item.quote_or_fact,
            "credibility": item.credibility,
            "verifiability": item.verifiability,
            "url": item.url,
        }
        for item in evidence_items
    ]

    sources_markdown = _render_sources_digest(event, evidence_rows, sources, uncertainties)
    mini06_markdown = _render_mini06_report(
        output_date=output_date,
        event=event,
        thesis=thesis,
        analogs=analogs,
        mini06=mini06,
        evidence_path=f"sources/{evidence_filename}",
        timeline=timeline,
        counter_hypotheses=counter_hypotheses,
        gate=gate,
    )
    memo_markdown = _render_ic_memo(
        output_date=output_date,
        event=event,
        thesis=thesis,
        gate=gate,
        evidence_path=f"sources/{evidence_filename}",
        evidence_score=gate_eval.evidence_score,
        support_score=getattr(gate_eval, "support_score", None),
        counter_score=getattr(gate_eval, "counter_score", None),
        gate_rationale=gate_eval.rationale,
    )

    sources_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)
    evidence_path.write_text(sources_markdown, encoding="utf-8")
    mini06_path.write_text(mini06_markdown, encoding="utf-8")
    memo_path.write_text(memo_markdown, encoding="utf-8")

    print(f"Sources digest written: {evidence_path}")
    print(f"Mini-06 report written: {mini06_path}")
    print(f"IC memo written: {memo_path}")

    if args.writeback:
        if args.hypothesis_id:
            registry_path = repo_root / "meta" / "hypotheses_registry.md"
            update_hypotheses_registry(
                registry_path,
                args.hypothesis_id,
                f"sources/{evidence_filename}",
                output_date,
            )
        if args.opportunity_title:
            opportunity_path = repo_root / "distilled" / "opportunity_map.md"
            upsert_opportunity_block(
                opportunity_path,
                event_id,
                args.opportunity_title,
                gate,
                mini06["tripwire"],
                mini06["probe_48h"],
                mini06["probe_7d"],
                mini06["probe_30d"],
                f"sources/{evidence_filename}",
                f"world_understanding/event_reasoning_runs/{mini06_filename}",
            )


if __name__ == "__main__":
    main()
