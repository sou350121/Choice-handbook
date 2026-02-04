# Event Reasoning Writeback Rules

目的：保证“事件推理”结果能回写到 `meta/` 与 `distilled/`，形成可迭代闭环。

## 1) 允许的回写目标

- `meta/hypotheses_registry.md`（新增或更新 1 条 H-XXXX）
- `distilled/opportunity_map.md`（更新 Gate/Tripwire/Bound/探针入口）
- `distilled/core_hypotheses.md`（仅当事件提升到“核心猜想”级别时才更新）

## 2) 回写原则

- **只追加证据，不覆写旧证据**（遵循 `meta/hypotheses_registry.md` 的规则）
- **明确“支持/反证/不确定”**：新证据必须标注它对旧猜想的影响
- **Gate 变化必须写触发条件**：从 Gate2→Gate3 或 Gate2→Gate1 都要写清楚“触发原因”

## 3) 最小回写格式（示例）

### Hypotheses Registry

```
核心证据（links，按时间追加）: ... / sources/YYYY-MM-DD_event_reasoning_<event_id>.md
反证信号（出现就降级）: ...
下一步验证（最小动作）: 48h/7d/30d 探针
```

### Opportunity Map

```
- **当前 Gate**：Gate 2（买信息期权）
- **最短探针**：48h/7d/30d
- **停机点（First Tripwire）**：...
```

