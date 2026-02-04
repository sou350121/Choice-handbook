# YYYY-MM-DD | Event Reasoning | <event_title>

> Scope: <scope>  
> Market: <market>  
> Gate: <Gate1/2/3>  
> Support evidence score (avg): <0.0-?> | Counter evidence score (avg): <0.0-?>  
> Evidence: `sources/YYYY-MM-DD_event_reasoning_<event_id>.md`

## 01 Snapshot（3 句内）

- 发生了什么（事实）
- 为什么重要（机制）
- 你的初步 Gate（注意力/仓位口径；若反证同样强，保持 Gate 2 并写清 Tripwire/Bound）

## 02 Evidence Table（证据表）

| time | source_type | claim | quote_or_fact | credibility | verifiability | url |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | high/med/low | how_to_verify | ... |

> 标注规则：如果某条证据是“反证/制衡信号”（例如：仍在 eligible/qualified/approved list；仍在公共项目落地），请在对应 YAML 的 `tags` 里加 `counter_evidence`，并在此处显式标注“(counter)”。  

## 03 Timeline（时间线）

- T-1: ...
- T0: ...
- T+1: ...

## 04 Mechanism Chain（因果链）

用箭头写出机制链条（供给/需求/监管/资金/预期）：

```
<event> -> <mechanism_1> -> <mechanism_2> -> <market_impact>
```

## 05 Counter Hypotheses（3 条反证路径）

1) ...
2) ...
3) ...

## 06 Gate + Tripwire/Bound/Spiral

- **T0-Analog (Case Atlas)**: <11.x/12.x/13.x> + <11.x/12.x/13.x>
- **First Tripwire**: ...
- **Catastrophic Bound**: ...
- **Death Spiral**: ...
- **最短探针**: 48h / 7d / 30d

## 07 Next Probes（最小验证动作）

- 48h: ...
- 7d: ...
- 30d: ...

## 08 Writeback Targets（可选）

- `meta/hypotheses_registry.md`: 更新 H-XXXX（支持/反证/不确定）
- `distilled/opportunity_map.md`: Gate/Tripwire/Bound/探针更新

## 09 Scenarios（情景树：带概率 + 可观测指标）

> 目的：把“预测”变成可审计的分支与观测量，而不是一句结论。

**1) Base**（概率/时间窗）
- 发生条件:
- 事件展开:
- 市场影响:
- 可观测指标（确认进入该分支）:
  - ...

**2) Downside**（概率/时间窗）
- ...

**3) Upside**（概率/时间窗）
- ...

