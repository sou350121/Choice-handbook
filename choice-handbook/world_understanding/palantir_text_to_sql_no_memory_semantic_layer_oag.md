# Palantir 式“问数”为什么可靠：不让模型“回忆”，而是让它“去查”（语义层 × 工具 × 审计）

> 来源 digest：`sources/2026-02-04_palantir_text_to_sql_no_memory_ontology_oag_paste.md`  
> 目标：把 Text-to-SQL 从“模型会不会写 SQL”改写成“系统能不能交付正确、可解释、可追溯的答案”。

---

## 概述（这篇解决什么误区）

- **误区 A：以为 Text-to-SQL 是一个“prompt/模型”问题**  
  实际上它是 **语义层 + 权限 + 工具约束 + 审计** 的系统工程。
- **误区 B：把 LLM 当数据库**  
  一旦让模型“回忆数字”，你就把正确性押在不可控的生成上。
- **误区 C：只要正确率，不要可追溯**  
  企业真正要的是：错了能定位到哪一步、哪条数据、谁改了什么。

核心结论：**可靠问数 = 语义层（对象/指标）+ 确定性执行（工具/计算）+ 全链路审计（lineage/observability）**。

---

## 框架/模型（可执行版）

### 1) “No Memory, Always Query”——禁止模型当数据源

- **原则**：LLM 不产出数字；LLM 只产出“查询/计算/行动”的调用计划（plan）。
- **对应工程动作**：
  - 把“生成 SQL”改成“调用指标/动作 API”
  - 把“复杂计算”交给 Python sandbox / 确定性函数

**适用**：任何需要对数字负责、需要审计、需要权限隔离的企业场景。  
**不适用**：纯探索性讨论、没有决策后果的头脑风暴（可以容忍幻觉）。

### 2) 语义层是唯一真理（Ontology / Semantic Layer / Metric Store）

把“表/字段/SQL”替换成“对象/指标/动作”，把开放世界降维成封闭接口：

- **对象（Objects）**：工厂、订单、客户、供应商……（企业内部的“名词”）
- **指标（Metrics）**：Revenue、On-time delivery rate……（企业内部的“可重复定义”）
- **动作（Actions）**：触发一次确定性的查询/写回/审批/工单（企业内部的“动词”）

**关键效果**：用户问的是“业务语言”，系统执行的是“语义层”，而不是让 LLM 在物理表里乱撞。

对应一手锚点：
- Palantir Ontology 文档（语义层/对象概念）：`https://www.palantir.com/docs/foundry/ontology/overview/`
- Databricks Business Semantics / Metric Views（指标语义层）：`https://www.databricks.com/product/unity-catalog/business-semantics`

### 3) 确定性工具（Tool Use）——把“写 SQL”变成“按按钮”

将高风险的自由生成缩到低风险的“受控调用”：

- **Bad**：LLM 直接生成 `SELECT ... JOIN ...`，并自行汇总/计算  
- **Good**：LLM 选择已定义的 metric / function / action：  
  - `get_metric("Revenue", region="China", timeframe="last_month")`  
  - `sum_sales(region="China")`  
  - 或者调用“受控 SQL 模板工具”（参数化、可测试、可权限控制）

当业务逻辑复杂（同比/环比/分组、异常处理、复用函数）时，把计算交给：
- **Python sandbox / 确定性函数**（可单测、可回归）

### 4) “Show your work”——审计/可观测是企业敢用的门槛

你要的不是“看起来像对”，而是**错了能定位**：

- **执行路径可视化**：每次问数都能还原成一条执行 DAG（检索/查询/计算/聚合/过滤/权限）
- **可追溯到数据来源**：至少能追到对象/指标定义；最好能追到行级/列级 lineage（取决于平台能力）
- **可观测**：run history / tracing / logs / token usage / errors（能做治理与成本控制）

对应一手锚点：
- Palantir AIP Observability：`https://palantir.com/docs/foundry/aip-observability/overview/`
- Palantir Workflow Lineage（依赖与数据流）：见 Palantir docs “workflow lineage” 相关页面

---

## Text-to-SQL 的 3 类失败模式 → 5 条工程金标准（把文章翻译成门禁）

### 失败模式 1：语义歧义（人没说清）

**门禁**：低置信度必须澄清，不许硬答。  
**实现**：交互式澄清（多选题式）：
- “最好销售”=销售额/毛利/净利？时间窗=本月/季度/全年？

### 失败模式 2：Schema 复杂（机器不知道怎么连）

**门禁**：LLM 永远不直面上千张物理表；必须走语义层或 schema linking。  
**实现**：
- 术语表：华东 ↔ East_China
- 列值样本：top-K distinct values / sample rows（受权限控制）
- 受控 join 路径：把“可 join 的键”变成白名单

### 失败模式 3：幻觉（机器瞎写/瞎算）

**门禁**：任何数字必须来自确定性执行（query/compute），并可追溯。  
**实现**：
- 工具化（metrics/functions/actions）
- 执行报错回传重写（但每次重写仍受控）
- 空集/异常值要有“解释与降级策略”（例如：提示口径、建议放宽过滤条件）

---

## 可验证预测（行业会怎么走）+ 观察信号

### 预测（更可能发生的 3 件事）

1) **Text-to-SQL 会“降级”为能力的一小部分**：主战场转向语义层与可审计执行链。  
2) **SQL 的地位下降，Python/DSL/受控函数上升**：因为复杂逻辑更可测试、更好调试。  
3) **企业 AI 的护城河变成“治理与可观测”**：权限/lineage/成本/回归评测决定能不能规模化。

### 观察信号（出现就确认趋势在发生）

- 语义层产品（metric views/semantic models/ontology）成为企业数据栈标配
- 平台把“LLM 输出”改成“可执行计划（plan）+ 工具调用轨迹（trace）”
- 企业开始用 evals/observability 把问数质量做成 SLO（正确率/可追溯率/澄清率/失败率/成本）

---

## 下一步（最小动作：7 天内可做）

- **做一个最小语义层**：先定义 10 个核心指标 + 20 个常用维度（时间/区域/渠道/客户），禁止直接写 SQL
- **做一个受控工具层**：把 20 个最常问问题变成 `get_metric()/drilldown()` 这类确定性接口
- **把审计做出来**：每次回答必须输出：查询计划、实际执行、数据来源链接、错误/空集处理

---

## 退出条件 / 重启条件（把“上线风险”写死）

- **退出条件（停机点）**：
  - 关键指标问数出现不可追溯答案（无来源/无计划）达到阈值（例如连续 3 次或一周内 >X%）
  - 权限/数据泄露风险出现（任何越权访问/敏感字段暴露）
  - 成本失控（token/查询/计算成本超预算且无法归因优化）
- **重启条件**：
  - 语义层覆盖扩大（核心指标覆盖率>Y%）+ 回归评测通过
  - 可观测链路完整（plan/trace/logs/lineage）并能定位错误根因

