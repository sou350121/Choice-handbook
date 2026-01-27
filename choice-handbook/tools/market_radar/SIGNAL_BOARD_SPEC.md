# Signal Board Spec（Market Radar 的“信号板规范”）

目标：把“可能会发生的结构变化”压成一张可持续更新的信号板，并把它**强制翻译**成：
- **Gate（1/2/3）**
- **First Tripwire / Catastrophic Bound / Death Spiral**
- **最短探针（7d/30d）**

> 原则：信号板不是为了“说服”，而是为了**提前看见**与**能退出**。

---

## 1) 最小字段（每个主题必须有）

- **universe**：主题名（文件名与输出文件名都用它）
- **tickers**：该主题下用作“形态代理”的标的集合（不等于投资建议）
- **signals**：信号定义（每条信号都要能被观测、能落到阈值）
- **thresholds**：阈值（触发 Tripwire/升级 Gate 的门槛）
- **cadence**：更新频率（7d/30d）
- **writeback**：回写规则（这次 run 要更新哪些 `H-XXXX`、要如何更新 `opportunity_map`）

---

## 2) Gate 映射（默认）

Market Radar 里的 `score` 是“信号强度/异常度”的粗指标（不是收益预测）。

- **Gate 1（淘汰）**：score 低且无结构信号（不值得消耗注意力）
- **Gate 2（买信息期权）**：score 中等或有结构信号（值得做信号板/最短探针）
- **Gate 3（分段下注）**：score 高且信号彼此一致（仍要写退出阈值；不等于价格路径确定）

默认阈值（可在主题里覆盖）：
- Gate 1: score ≤ 2
- Gate 2: 3 ≤ score ≤ 6
- Gate 3: score ≥ 7

---

## 3) Tripwire/Bound/Spiral 的生成原则

- **Tripwire**：最早的坏信号（或最早的相变信号）。必须写成阈值化、可观测。
- **Bound**：不可逆红线（触发就退出/止损/停机）。
- **Spiral**：螺旋机制（为什么会越走越坏/越走越贵/越走越挤）。

优先从“硬约束收紧”生成 Tripwire：交期、良率、认证周期、事故率、融资条件、平台规则等。

---

## 4) 当前实现（MVP）的信号来源

MVP 先用两类信号（能自动抓取 + 可稳定跑通）：

1) **价格/量能**（Yahoo/Futu）：
- 1d/5d/20d momentum（异常上涨/异常下跌）
- volume/avg20（成交量尖峰，作为“注意力/拥挤度”代理）

2) **文本关键字**（SEC filings + RSS 标题）：
- supplychain / platform / financial 三桶关键字命中数（作为“结构主题出现”代理）

> 这不是最终形态。后续你可以把“交期/报价/库存/事故率/Capex/bit growth”等真实产业信号接进来（但需要更具体的数据源）。

---

## 5) 两个样板主题（已内置配置）

- `aiinfra_bottleneck_shift`：电力/散热/网络/封装/内存的瓶颈迁移（覆盖“内存价格爆炸”类事件）
- `model_price_war_profit_pool_shift`：模型价格战→盈利池迁移（SoR/数据围墙/分发/默认入口）

