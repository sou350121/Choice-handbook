# /event-reasoning — Choice Handbook 真实事件推理

面向：使用 Cursor 交互的大模型用户。  
目标：把“正在演进的真实事件”变成 **可审计证据表 + 可下注情景树 + 停机点**（Tripwire/Bound），并生成 1 页 IC memo。

## 你对模型怎么说（复制粘贴）

请使用 `choice-handbook/tools/event_reasoning` 的工作流，帮我把下面事件做成可执行的事件推理：

1) 把我的描述整理成一个输入 YAML，落盘到：`choice-handbook/tools/event_reasoning/examples/<event_id>.yaml`  
2) 如果信息不够，请只追问“最少 3 个”缺口：  
   - market（市场范围）  
   - 3 个情景（base/bull/bear：概率/时间窗/触发条件 + observables）  
   - Tripwire/Bound（可观测、可执行的停机点）  
3) 把我给的链接写进 `evidence`。如果是反证（例如仍在合格清单/仍在项目落地），给该条加：`tags: [counter_evidence, ...]`  
4) 运行：`python choice-handbook/tools/event_reasoning/src/event_reasoning/run.py --input <yaml_path>`  
5) 把输出文件路径回给我（3 个）：sources digest / IC memo / mini06  

这是事件描述与线索（含链接）：
<粘贴你的事件文本与链接列表>

## event_type 快速选型（建议你在事件描述里点名一个）

- **监管/政策（regulatory / macro_policy）**：规则/许可/采购口径/税收与利率等改变，影响准入与传导路径
- **资本配置/供给冲击（capital_allocation_signal）**：回购/增发/配股/减持计划/股权结构变化，重定价“供给过hang/信任”
- **供需冲击（supply_demand_shock）**：价格/库存/产能利用率/运价/订单与渠道数据驱动的周期拐点
- **技术突破（tech_breakthrough）**：产品/论文/基准/专利触发的成本曲线或能力跃迁

> 如果你不确定，就写：`event_type: n/a`，让模型按证据与机制选择最贴近的一类。

## 情景必须“可观测”（observables）

请在每个情景下补一段 `observables`（列表）：写清楚“出现哪些披露/数据，就意味着正在进入该分支”，让预测可审计、可回滚。

## 你得到什么（默认输出）

- `choice-handbook/sources/YYYY-MM-DD_event_reasoning_<event_id>.md`（证据表，可审计）
- `choice-handbook/world_understanding/event_reasoning_runs/YYYY-MM-DD_<event_id>_memo.md`（1 页 IC memo）
- `choice-handbook/world_understanding/event_reasoning_runs/YYYY-MM-DD_<event_id>_mini06.md`（Tripwire/Bound/Spiral/探针）

## Gate 的口径（避免误读）

- Gate 是 **注意力/仓位口径**，不是“官方定性/已经坐实”。
- Gate 取决于两类证据：Support evidence vs Counter evidence（反证用 `counter_evidence` 标记）。

