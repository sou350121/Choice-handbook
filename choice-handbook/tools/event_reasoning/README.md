# Event Reasoning Tool (MVP)

目标：把“真实事件推理”落到可审计、可回滚的**深度尽调式 memo**（证据表 → 时间线 → 机制链 → 反证 → Gate）。

## 0) 给 Cursor 用户的用法（推荐）

你不需要先学 YAML。你可以直接在 Cursor Chat 里这样发起：

- **最短发起句**：  
  “请用 `choice-handbook/tools/event_reasoning` 把下面事件跑一遍（生成 memo/mini06/证据表），并把输入 YAML 也落盘到 `tools/event_reasoning/examples/`：……”

模型应该做的事（你可以用它作为验收清单）：
- **把你的自然语言事件**转成一个 `examples/<event_id>.yaml`
- **要求你补 3 个关键信息**（如果缺）：市场（market）、情景（3 个）、Tripwire/Bound（停机点）
- **把你给的链接**写入 `evidence`；如果某条是“反证/仍在可用清单/仍在落地”，给它 `tags: [counter_evidence, ...]`
- **运行脚本**并把输出文件路径回给你

## 0.1) Gate 的含义（防误读）

- **Gate = 注意力/仓位口径**，不是“已经坐实/官方定性”。
- Gate 由两类证据共同决定：
  - **Support evidence**：支持主论点的证据强度
  - **Counter evidence**：反证主论点的证据强度（通过 `counter_evidence` tag 标记）
- 直觉：**支持强但反证也强 → Gate 2（继续跟踪 + 条件动作）**，避免“强反证把 Gate 抬到 3”的误判。

## 0.2) event_type 快速选型（推荐）

- **regulatory**：监管/合规/准入变化（最常见：采购口径、名单、调查、禁令、补贴资格）
- **macro_policy**：宏观政策与利率/财政（“传导链与滞后”比新闻更关键）
- **capital_allocation_signal**：资本配置与供给冲击（回购/减持/配股/增发/再融资；核心是“供给过hang/信任”）
- **supply_demand_shock**：供需与库存周期（价格/库存/产能利用率/运价/订单与渠道数据）
- **tech_breakthrough**：技术/产品拐点（论文/发布/基准/专利；核心是成本曲线与集成阻力）

不确定就先选你“最担心的传导路径”对应的类型；选错也没关系——关键是把 **scenarios + observables + Tripwire/Bound** 写清楚。

## 1) 输入格式（YAML/JSON 二选一）

**最小输入（YAML）**：

```yaml
event:
  id: autel_energy_us_investigation
  title: US_Investigates_Autel_Energy_EV_Chargers
  date: 2025-05-19
  scope: US_EV_charger_national_security_review
  market: global_multi
  tags: [regulatory, geopolitics, infrastructure, critical_infra]
  analogs:
    - yearbook/case_atlas_public_policy_state_capacity_06.md

evidence:
  - time: 2025-05-19
    source_type: congressional_letter
    url: https://selectcommitteeontheccp.house.gov/.../05.19.25_Autel%20Congressional%20Investigation%20letter_FINAL.pdf
    claim: Lawmakers_request_investigation_and_possible_entity_list_addition
    quote_or_fact: Letter_asks_Commerce_and_Defense_to_investigate_Autel_Energy_links_and_consider_Entity_List
    credibility: high
    verifiability: read_primary_pdf
    tags: [regulatory, national_security]
```

**最小输入（JSON）**字段与上面一致。

## 2) 输出（默认）

- `choice-handbook/sources/YYYY-MM-DD_event_reasoning_<event_id>.md`
  - 证据表（Evidence Table）+ 不确定性 + 关键主张
- `choice-handbook/world_understanding/event_reasoning_runs/YYYY-MM-DD_<event_id>_mini06.md`
  - mini-06 门禁版：T0-Analog / Tripwire / Bound / Spiral / 最短探针

可选：
- `meta/hypotheses_registry.md`：新增/更新 1 条可证伪猜想
- `distilled/opportunity_map.md`：更新 Gate/Tripwire/Bound/探针入口

## 3) 关键约定（只保留会影响结果的）

- **反证必须标**：如果某条证据是反证/制衡信号（仍在合格清单、仍在公共项目落地等），请在该条 `tags` 里加 `counter_evidence`。  
- **Gate 口径**：Gate 是注意力/仓位口径；当支持证据强但反证也强时，默认停在 Gate 2（继续跟踪 + 条件动作）。
- **情景必须可观测**：`thesis.scenarios[]` 建议增加 `observables`（列表），写“哪些披露/数据出现，就意味着进入该分支”，让预测可审计、可回滚。

## 4) 运行方式（示例）

```bash
python choice-handbook/tools/event_reasoning/src/event_reasoning/run.py --input path/to/event.yaml
```

## 5) 设计原则

- 证据优先：每个主张至少 1 条一手文件或 2 条独立来源。
- 反证优先：先写最短反证路径，再谈结论。
- Gate 不是投资建议：它只表示“是否值得继续耗注意力”。

