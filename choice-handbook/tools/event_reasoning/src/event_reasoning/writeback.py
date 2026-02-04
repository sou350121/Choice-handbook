from __future__ import annotations

from pathlib import Path


def _normalize_cell(text: str) -> str:
    return text.strip()


def update_hypotheses_registry(path: Path, hypothesis_id: str, evidence_link: str, updated_date: str) -> bool:
    if not path.exists():
        return False
    lines = path.read_text(encoding="utf-8").splitlines()
    updated = False
    for idx, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 10:
            continue
        if cells[1] != hypothesis_id:
            continue
        evidence_cell = cells[6]
        if evidence_link not in evidence_cell:
            evidence_cell = f"{evidence_cell} / {evidence_link}" if evidence_cell else evidence_link
        cells[6] = evidence_cell
        cells[9] = updated_date
        rebuilt = "| " + " | ".join(cells[1:-1]) + " |"
        lines[idx] = rebuilt
        updated = True
        break
    if updated:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return updated


def upsert_opportunity_block(
    path: Path,
    event_id: str,
    title: str,
    gate: str,
    tripwire: str,
    probe_48h: str,
    probe_7d: str,
    probe_30d: str,
    evidence_path: str,
    mini06_path: str,
) -> bool:
    if not path.exists():
        return False
    content = path.read_text(encoding="utf-8")
    marker_start = f"<!-- event_reasoning:auto:{event_id}:start -->"
    marker_end = f"<!-- event_reasoning:auto:{event_id}:end -->"
    block = "\n".join(
        [
            marker_start,
            f"### {title}（Event Reasoning: {event_id}）",
            f"- **当前 Gate**：{gate}",
            f"- **最短探针**：48h: {probe_48h} / 7d: {probe_7d} / 30d: {probe_30d}",
            f"- **停机点（First Tripwire）**：{tripwire}",
            f"- **入口**：`{evidence_path}` / `{mini06_path}`",
            marker_end,
        ]
    )
    if marker_start in content and marker_end in content:
        before = content.split(marker_start)[0].rstrip()
        after = content.split(marker_end)[1].lstrip()
        new_content = f"{before}\n{block}\n{after}"
    else:
        insert_point = content.find("## 风险墙")
        if insert_point == -1:
            new_content = content.rstrip() + "\n\n" + block + "\n"
        else:
            new_content = content[:insert_point].rstrip() + "\n\n" + block + "\n\n" + content[insert_point:]
    path.write_text(new_content, encoding="utf-8")
    return True
