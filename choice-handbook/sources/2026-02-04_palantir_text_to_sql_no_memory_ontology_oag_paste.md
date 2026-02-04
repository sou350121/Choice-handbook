# Palantir 为什么不让 AI “回忆”数据：Text-to-SQL 的真实解法（用户粘贴 + 一手锚点）

> 说明：本文基于用户粘贴的中文文章做“可回查 digest”，并补充关键主张的一手/官方资料锚点（Palantir Docs / Databricks Docs）。
> 目标：把“问数/Text-to-SQL”从模型神话拉回 **系统工程**：语义层（Ontology/Semantic Layer）+ 确定性工具（Tooling）+ 全链路审计（Audit/Observability）。

## 01 Snapshot（先把结论边界说清）

- **文章主张**：不要把数据库直接扔给 LLM 让它“凭记忆出答案”，而要让 LLM **去查**（tool use），并把答案可追溯到数据/执行路径。
- **可核验点（已补锚）**：
  - Palantir Foundry 的 **Ontology** 被官方定义为语义层（对象/属性/链接/动作）。
  - Palantir 文档存在 **Ontology-augmented generation**（OAG）口径（官方称 “Ontology augmented generation / Ontology-augmented generation”）。
  - Palantir 有 **AIP Observability / Workflow Lineage** 等“可观测/可追溯”的产品文档。
  - Databricks 有 **Business Semantics / Metric Views**（语义层/指标定义）作为“不要让 LLM 直接写 SQL”的工程化路径之一。
- **这份材料的盲区**：用户粘贴文未提供原始出处；文章里部分措辞（例如“准确性公式”“从不让 AI 回忆数据”）更像解释性总结，需要以官方文档与实际系统实现为准。

## 02 Evidence Table（证据表：一手优先）

| time | source_type | claim | quote_or_fact | credibility | verifiability | url |
|---|---|---|---|---|---|---|
| 2026-02-04 | user_paste | 用户粘贴稿：Palantir 通过 AIP + Ontology + 审计来解决 Text-to-SQL 幻觉 | 二手阐释文本（未含原始链接） | low | narrative_only | n/a |
| 2026-02-04 | palantir_docs | Palantir Ontology 文档（Ontology building / core concepts）描述对象、属性、链接、动作等语义层概念 | 官方文档：Ontology 概览与核心概念 | high | read_primary_docs | https://www.palantir.com/docs/foundry/ontology/overview/ |
| 2026-02-04 | palantir_docs | Palantir 存在 Ontology-augmented generation（OAG）文档口径 | 官方文档页面标题/内容：Ontology augmented generation | high | read_primary_docs | https://www.palantir.com/docs/foundry/ontology/ontology-augmented-generation |
| 2026-02-04 | palantir_docs | Palantir AIP Observability 提供执行历史、分布式追踪、日志、性能监控等 | 官方文档列出关键能力点（execution history/tracing/logging） | high | read_primary_docs | https://palantir.com/docs/foundry/aip-observability/overview/ |
| 2026-02-04 | databricks_docs | Databricks 提供 Business Semantics / Metric Views 作为语义层/指标一次定义多处复用 | 官方产品/文档：Business semantics & metric views | high | read_primary_docs | https://www.databricks.com/product/unity-catalog/business-semantics |

## 03 可抽取资产（你可以直接复用的“工程门禁”）

### A. 一句话原则（反幻觉）

- **LLM 负责理解与编排，不负责当数据库**：永远让它“调用确定性工具去查/去算”，而不是在 prompt 里“回忆数字”。

### B. 架构三件套（从 Prompt Engineering → System Engineering）

1) **语义层**：把物理表映射成业务对象/指标（Ontology / Semantic Layer / Metric Store）  
2) **确定性工具**：把开放式 SQL 写作变成“封闭式指标/动作调用”（tool use）  
3) **审计与可观测**：答案必须可追溯到执行 DAG 与数据来源（lineage/observability）

### C. Text-to-SQL 常见失败模式（可当 checklist）

- **语义歧义**：人没说清（需要澄清）
- **schema 复杂**：模型不知道该 join 哪些表/字段（需要 schema linking / 术语映射）
- **幻觉**：模型编数字/编字段/编表（需要工具化 + 审计）

## 04 用户粘贴原文（未改动）

为什么 Palantir 从不让 AI “回忆”数据？聊聊 Text-to-SQL 的真实解法
最近和不少做企业服务的朋友聊到“问数”（Text-to-SQL）场景，大家的共识惊人的一致：直接把数据库扔给大模型，简直就是灾难。

要么 SQL 写错，要么字段对不上，最可怕的是它一本正经地给你编造了一个数字。

在这方面，大数据领域的“老大哥” Palantir 给出的答案非常值得玩味：在他们的架构里，LLM 被“降级”了。

Palantir 并不依赖 LLM 直接生成答案，而是把 LLM 当作一个推理引擎（Reasoning Engine）和编排器（Orchestrator）。

简单说：Palantir 从不让 AI “回忆”数据，而是让 AI “去查”数据。

这背后的逻辑其实是把 Prompt Engineering 升级为了 System Engineering。今天我们就拆解一下 Palantir 的做法，以及目前业界解决“AI 瞎编 SQL”的几条金标准。

一、 Palantir 的解法：把 LLM 关进笼子里
Palantir 的核心机制主要由 AIP（AI Platform） 和 Foundry 本体（Ontology） 共同支撑。他们有一条关于准确性的公式：

准确性 = 高质量本体 (Data) + 确定性工具 (Logic) + 全链路溯源 (Audit)

具体是怎么跑通的？

1. 核心基石：本体（Ontology）是唯一真理
Palantir 坚决反对把企业私有数据灌进 LLM 去训练。那样做不仅有泄露风险，而且数据更新极其滞后。

他们建立了一个“语义层”——也就是“本体”。

在这一层，数据不再是冷冰冰的表结构，而是被映射为具体的对象（Objects），比如“一个工厂”、“一份订单”。当用户问“工厂产量”时，系统查询的是经过清洗治理的结构化对象，而不是在文本海里大海捞针。

2. LLM 只负责“按按钮”（Tool Use）
这是 RAG 的进阶版，Palantir 称之为 OAG（本体增强生成）。

举个例子，用户问：“中国区销量总和是多少？”

普通 LLM： 可能会自己尝试做加法（极其容易算错），或者产生幻觉。

Palantir AIP： 识别出意图是“计算总和”，它绝对不会自己算，而是生成一段代码去调用一个预定义的工具，比如 sum_sales(region="China")。

LLM 在这里只是一个“翻译官”，它负责理解人话，然后去按下一个确定性的按钮。

3. 拒绝黑盒：Show Your Work
为了彻底解决信任问题，Palantir 强调全链路溯源。

在它的界面里，用户不仅能看到答案，还能看到 AI 的执行逻辑图（DAG）：

Step 1: 识别对象“供应商 A”

Step 2: 调用工具查询“延迟交货率”

Step 3: 对比历史数据

如果你觉得数字不对，点一下就能追溯到原始的数据行（Row-level）。这种“白盒化”是企业敢用 AI 的前提。

二、 业界共识：如何构建高容错的“问数”架构？
除了 Palantir，包括 Databricks 和 AWS 在内的头部玩家现在都有一个共识：不要试图训练一个完美的模型，而是要构建一个容错的架构。

解决 Text-to-SQL 的核心挑战通常是三个：语义歧义（人没说清）、Schema 复杂性（机器看不懂表）、幻觉（机器瞎写）。

以下是目前经过实战验证的 5 种核心策略，按重要性排序：

1. 构建“语义层” (Semantic Layer) —— 这是防线
不要让 LLM 直接面对成百上千张物理表（比如 t_fct_order_2023_v2 这种鬼名字）。

你需要在一个中间层（Metric Store 或 Headless BI）把逻辑封装好。

Bad Case: 让 LLM 去拼写 SELECT sum(amt) FROM...

Good Case: 让 LLM 调用语义接口 get_metric('Revenue', timeframe='last_month')

把“开放式的写 SQL”变成“封闭式的选指标”，准确率直接起飞。

2. 增强上下文 (Schema Linking)
如果非要查库，请教会 LLM 看懂你的数据库。

注入列值样本： 比如数据库存的是 East_China，用户问“华东”。如果不通过 RAG 检索把这两个词关联起来喂给 LLM，它永远查不到。

业务术语表： 企业的“黑话”要映射给 AI。告诉它，“大客户”的定义不仅是“大”，而是“年单量 > 100万”。

3. 慢思考：多步推理与自查
模仿人类分析师，不要试图一步到位。

CoT (思维链)： 强制 LLM 在写 SQL 前先解释一遍：“用户想看 X，涉及 A 表和 B 表，连接键是 id...”。

自我修正： SQL 报错了？没关系，把错误信息回传给 LLM 让它重写。查出来是空集？可能是条件太严苛，让 AI 自动放宽条件重试。

4. 交互式澄清 —— 解决“人”的问题
很多时候不准确，是因为人自己没问清楚。

当置信度低时，Agent 不应该硬答，而应该反问：

“您说的‘最好的销售’，是指销售额最高，还是利润率最高？是看本月还是全年？”

5. 确定性执行环境 (Python Sandbox)
对于复杂的同比、环比、预测，SQL 其实很吃力。

现在的趋势是 Python > SQL。让 LLM 生成 Pandas 代码，在沙箱里跑。Python 处理复杂逻辑更强，也更容易进行单元测试和调试。

写在最后
归根结底，AI Agent 在数据分析领域的应用，正在从“神话模型能力”回归到“扎实的软件工程”。

一端是用 语义层 把数据治理得井井有条；另一端是用 Agent 推理架构 把大模型的能力约束在逻辑的轨道上。只有这样，AI 才能从一个“胡言乱语的聊天机器人”，变成真正可信的数据分析师。

