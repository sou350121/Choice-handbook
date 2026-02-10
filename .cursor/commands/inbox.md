# /inbox — Choice Handbook 默认入口（自动路由：文章 / 事件 / 06 重武器）

面向：使用 Cursor 交互的大模型用户。  
目标：你把任何材料贴进来，我自动判断你想要的产出，并把结果落盘到 `choice-handbook/`。

## 你对模型怎么说（复制粘贴）

请把下面输入当作我的 `inbox`，按 `choice-handbook` 的默认路由处理，并把产物落盘（给出文件路径）：

### 0) 先做路由判断（只用 1 条规则）

- **若我明确写了**：穿越者投资判官 / 最大必然性 / 收费站 / 政治情境树 / 低估检验 / 3–5 年上升空间 → 走 **Traveler Judge**（等同 `/traveler-judge`）。  
- **否则若我明确写了**：BTC / 100x / 1000x / 终局 / Gate / 估值 / 路线图 → 直接走 **Framework 06**（等同 `/time-travel-06`）。  
- **否则若输入是“正在演进的真实事件”**（监管/政策/资本动作/供需/技术拐点，且需要情景树+停机点）→ 走 **Event Reasoning**（等同 `/event-reasoning`）。  
- **否则（默认）** → 走 **Article Processing（Framework 05 口径）**（等同 `/article-digest`）。  

> 如果你无法判断（极少数情况），只追问 **1 个**最小分流问题：\n> “这更像文章材料，还是正在演进的真实事件？”\n> 我回答后立即继续，不要追问更多。

### 1) 不同路由的默认交付（照做）

#### A) Article Processing（默认，05）

1) 生成 `sources` digest（保留原文 + 可核验锚点 + 可抽取资产 + 不确定性），落盘到：  
   `choice-handbook/sources/YYYY-MM-DD_<slug>_paste.md`
2) 生成 `world_understanding` 主文（机制/变量/情景+observables/探针/退出重启），落盘到：  
   `choice-handbook/world_understanding/<slug>.md`  
   - 必须包含：机制链（箭头）/ 变量表（≤10）/ 3 情景（概率+时间窗+observables）/ 48h-7d-30d 探针 / 退出条件+重启条件  
   - 知识工厂工序（强制）：补一段“重述/合并”（抽旧库 2–3 节点，写合并新表述 + 冲突点 + 最小探针）
3) 更新索引：  
   - `choice-handbook/sources/README.md`  
   - `choice-handbook/world_understanding/README.md`
4) 如果材料足够可证伪：新增/更新 1 条猜想到 `choice-handbook/meta/hypotheses_registry.md`（不确定就跳过，别硬写）。

#### B) Event Reasoning（事件推理）

按 `/event-reasoning` 命令执行：产出 sources 证据表 + IC memo + mini-06，并把输入 YAML 也落盘到 `choice-handbook/tools/event_reasoning/examples/`。

#### C) Framework 06（重武器）

按 `/time-travel-06` 命令执行：按 `choice-handbook/frameworks/06_time_travel_endgame_simulator.md` 固定标题完整输出（标题不可省），并落盘到：  
`choice-handbook/world_understanding/<slug>_endgame_06.md`  
必要时补 `sources` digest 与索引更新，并更新 `meta/hypotheses_registry.md`。

### 2) 回传格式（让我一眼看懂）

请按下面顺序回传（保持短）：  
- 你判定的路由：Article / Event / 06  
- 你新生成/更新的文件路径清单  
- 1 段 10 行以内摘要（可执行结论 + 最短探针 + 退出条件）  

这是输入全文与链接（若无链接也可以）：
<粘贴全文 / 要点 / 链接列表>

