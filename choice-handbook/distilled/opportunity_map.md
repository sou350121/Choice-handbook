# 机会图谱（Opportunity Map）

> 这是蒸馏层的“Top 候选入口”：把当前最值得跟踪的 3–5 个机会/主题按 **Gate（1/2/3）**、**最短探针**、**停机点** 排序。
>
> 更新方式：每次有新材料进入，先用 `frameworks/06_time_travel_endgame_simulator.md` 走一遍（T0→Now、Endgame Map、Gate），再把结果回写 `meta/`，最后在这里更新排序与 Gate。

---

<!-- market_radar:auto:us_ai_infra:start -->
## Market Radar (auto) — us_ai_infra
- Latest run: n/a
- Evidence: `sources/YYYY-MM-DD_market_radar_us_ai_infra.md`
- Mini-06: `world_understanding/market_radar_runs/YYYY-MM-DD_us_ai_infra_top3_mini06.md`
- Top US: n/a
- Top HK/SH/SZ: n/a

<!-- market_radar:auto:us_ai_infra:end -->

<!-- market_radar:auto:aiinfra_bottleneck_shift:start -->
## Market Radar (auto) — aiinfra_bottleneck_shift
- Latest run: n/a
- Evidence: `sources/YYYY-MM-DD_market_radar_aiinfra_bottleneck_shift.md`
- Mini-06: `world_understanding/market_radar_runs/YYYY-MM-DD_aiinfra_bottleneck_shift_top3_mini06.md`
- Top US: n/a
- Top HK/SH/SZ: n/a

<!-- market_radar:auto:aiinfra_bottleneck_shift:end -->

<!-- market_radar:auto:model_price_war_profit_pool_shift:start -->
## Market Radar (auto) — model_price_war_profit_pool_shift
- Latest run: n/a
- Evidence: `sources/YYYY-MM-DD_market_radar_model_price_war_profit_pool_shift.md`
- Mini-06: `world_understanding/market_radar_runs/YYYY-MM-DD_model_price_war_profit_pool_shift_top3_mini06.md`
- Top US: n/a
- Top HK/SH/SZ: n/a

<!-- market_radar:auto:model_price_war_profit_pool_shift:end -->

## Top 候选（按：非对称性 × 可验证性 × 生存性）

> 说明：这里的 “10x/100x/1000x” 是对 **机制上限** 的粗分档，不承诺收益路径与时间。

### 1) AI 应用赢家形态：SoR + 数据围墙/结果闭环（H-0013）

- **潜力档位**：更像 **10x–100x**（更多是“赢家形态收敛”的确定性，而非单票价格路径确定）  
- **当前 Gate**：**Gate 2（买信息期权）**  
- **为什么值得跟踪（1 句）**：模型趋同后，利润更可能沉到“系统记录 + 独家数据 + 定价权”，薄工具长期被挤压。  
- **最短探针（7d）**：用“护城河打分卡”评估 3 个候选（SoR 证据/闭环数据证据/seat→usage/outcome），写出 3 条反证信号。  
- **停机点（First Tripwire）**：目标公司在竞争加剧后出现 **留存与定价权持续下滑** 且不可逆；或关键数据并不独家/授权不稳。  
- **入口**：`distilled/core_hypotheses.md`（H-0013） / `distilled/high_certainty_decisions.md`（D-0009）

### 2) AI 供应链：交付瓶颈向封装/认证链条迁移（H-0002）

- **潜力档位**：更像 **10x**（硬约束驱动的结构机会，兑现更看周期与资本结构）  
- **当前 Gate**：**Gate 2（买信息期权）**  
- **为什么值得跟踪（1 句）**：算力兑现的硬门槛常在“能否按期交付”，而不是最前沿叙事。  
- **最短探针（30d）**：做“五段信号板”：交期/良率/认证/报价/外溢（每周更新一次）。  
- **停机点（First Tripwire）**：交期与报价 **长期回落且稳定**，外溢与第二路线不再形成可回归兑现。  
- **入口**：`distilled/core_hypotheses.md`（H-0002）

### 3) 规模化训练：稳定性硬约束成为默认（H-0001）

- **潜力档位**：更像 **10x**（对“训练范式与工程栈”的结构性确定性；适合“建造者/团队”）  
- **当前 Gate**：**Gate 2（买信息期权）**  
- **为什么值得跟踪（1 句）**：大规模下，能被保证的不变量会替代“调参好运”，稳定性指标板会成为标配。  
- **最短探针（7d）**：给任一训练栈加逐层 Amax + layer0 canary + 压力测试阈值，验证“loss 正常但内部漂移”能否被提前预警。  
- **停机点（First Tripwire）**：无约束混合在更大规模/更长训练/更激进工况下仍长期稳定，且跨 seed 回归性不差。  
- **入口**：`distilled/core_hypotheses.md`（H-0001） / `distilled/high_certainty_decisions.md`（D-0002）

### 4) 具身/机器人：数据基础设施优先于端到端信仰（H-0004）

- **潜力档位**：更像 **10x–100x**（一旦进入产业交付链条，复利来自数据与回归体系）  
- **当前 Gate**：**Gate 2（买信息期权）**  
- **为什么值得跟踪（1 句）**：迁移/恢复能力的关键在“关键窗口 + 失败分类 + 回归体系 + 可检索可版本化管道”。  
- **最短探针（7d）**：把数据做“可用”：关键窗口切片 + 失败分类 + 最小回归集 + 检索/版本化。  
- **停机点（First Tripwire）**：更 clean 的流程在迁移/恢复上持续胜出，且组织成本不线性增长（说明我们押错了主矛盾）。  
- **入口**：`distilled/core_hypotheses.md`（H-0004） / `distilled/high_certainty_decisions.md`（D-0003）

### 5) 汽车后市场：AI 诊断消费化 → 数据闭环 → 订阅/生态（H-0014）

- **潜力档位**：更像 **10x–100x**（若成为行业默认诊断入口；但受 OEM/合规硬约束）  
- **当前 Gate**：**Gate 2（买信息期权）**  
- **为什么值得跟踪（1 句）**：诊断是维修决策瓶颈；一旦“诊断→维修→结果”闭环数据成立，工具可能升级为订阅与生态平台。  
- **最短探针（30d）**：做一张信号板：订阅形态/续费线索、复访与案例增长、关键车系可用性、Right-to-Repair 与 OEM 动态、合规/责任事件。  
- **停机点（First Tripwire）**：OEM 协议/加密收紧导致核心车系不可用；或出现重大责任事故导致信任/合规成本急剧上升；或订阅续费不成立。  
- **入口**：`meta/hypotheses_registry.md`（H-0014） / `world_understanding/ai_auto_aftermarket_diagnostics_topdon_topfix.md`

---

## 候补跟踪（不进 Top5，但值得 Gate2 盯住）

### A) 人形机器人“开源基建”：可复现全栈底座 × 治理/认证价值捕获（H-0015）

- **潜力档位**：更像 **10x**（更偏“行业加速器/标准化底座”，上限取决于是否进入认证与交付链）
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：它把“人形从零造轮子”改写为“可复现、可回归的工程科学”，但成败取决于治理与复现成功率。
- **最短探针（7d）**：对 `Roboparty/roboto_origin` 做“可复现审计”（BOM/替代件/装配/调试/测试矩阵/版本治理/外部贡献闭环）。
- **停机点（First Tripwire）**：repo 长期失活 + 外部复现失败无闭环；或生态碎片化（分叉不兼容且不回流）。
- **入口**：`distilled/core_hypotheses.md`（H-0015） / `world_understanding/roboparty_roboto_origin_open_source_humanoid_infra.md`

### B) 代理人电商入口：对话式决策压缩 × 证据透明 × 结果闭环（H-0016）

- **潜力档位**：更像 **10x**（入口迁移大概率发生；超额收益取决于“闭环结果数据”是否形成复利）
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：从“货架”到“代理人”的迁移，把护城河推向交易/履约/退换货原因等结果数据；但极易被广告/GMV 价值捕获摧毁信任。
- **最短探针（30d）**：做“对话电商信号板”：对话→下单转化、复购链路长度、退货/差评原因、理由可追溯性、推理成本与延迟。
- **停机点（First Tripwire）**：对话推荐导致踩坑不降反升（退货/差评原因恶化）或推荐明显被商业激励扭曲。
- **入口**：`distilled/core_hypotheses.md`（H-0016） / `world_understanding/jd_ai_shopping_agentic_commerce.md`

### C) 具身评测基建：Benchmark as Infrastructure × 失败病历回归 × Real2Sim（H-0017）

- **潜力档位**：更像 **10x–100x**（若形成事实标准并能预测真机表现，上限巨大）
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：具身的 scaling 会被“可规模化评测/诊断”硬约束；掌握任务库+失败病历+物理对齐与抗刷榜治理的评测栈能形成长期复利。
- **最短探针（30d）**：做“评测基建信号板”：任务库规模/版本治理、hidden test/对抗集、失败分类字典、Real2Sim 对照证据、外部复现、漏洞披露与修复速度。
- **停机点（First Tripwire）**：评测与真机长期无相关；或刷榜漏洞无法封堵；或标准碎片化导致无法形成共同语言。
- **入口**：`distilled/core_hypotheses.md`（H-0017） / `world_understanding/world_labs_lightwheel_evaluation_driven_embodied.md`

### D) 桌面 Cowork（开源）：本地优先 × MCP 工具生态 × 执行权治理（H-0018）

- **潜力档位**：更像 **10x**（趋势大概率发生；超额收益取决于是否形成安全基线与可持续生态）
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：从“聊天”到“动手”的迁移正在发生；在 Apache-2.0 许可摩擦降低后，独立 app 的生死线更集中在 **默认最小权限/审计/回滚** 与平台吞并压力。
- **最短探针（7d）**：做 10 条桌面回归任务集（文件/网页/代码/文档）：记录成功率、事故率、平均耗时；同时核对 **审计导出/回滚/危险操作二次确认** 是否可用（写停机阈值）。
- **停机点（First Tripwire）**：任何越权/不可解释修改/误删事故；或许可证阻断生态；或平台原生能力以更低摩擦覆盖同等场景。
- **入口**：`distilled/core_hypotheses.md`（H-0018） / `world_understanding/eigent_open_source_cowork_desktop_mcp.md` / `world_understanding/clawdbot_local_first_gateway_zero_employee_company_06.md`

### E) 部署期安全再对齐：PTQ（量化）作为“最后一次低成本结构干预”（H-0019）

- **潜力档位**：更像 **10x**（工程确定性提升：把安全修复从训练侧迁到部署侧；不是资产级 1000x）
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：量化是上线必经步骤；若能在 PTQ 中稳定恢复微调造成的安全漂移，就能以固定成本显著降低多版本上线的维护负担与事故风险。
- **最短探针（7d）**：做四组对照（基座/微调/PTQ/修复 PTQ）+ unseen/adaptive 攻击 + 误拒率统计，写停机阈值。
- **停机点（First Tripwire）**：unseen/adaptive 无稳定增益；或误拒率显著上升导致产品不可用；或低比特量化下能力/安全同时恶化。
- **入口**：`distilled/core_hypotheses.md`（H-0019） / `world_understanding/q_realign_quantization_deployment_safety_realignment.md`

### F) 金库迁移：冻结/制裁风险 → 本地托管偏好 → 贵金属作为“退出权/保险层”（H-0026）

- **潜力档位**：更像 **1x–3x（保险层，不是 10x/100x 复利）**  
- **当前 Gate**：**Gate 2（买信息期权）**  
- **为什么值得跟踪（1 句）**：当“可被扣押性”进入风险定价，贵金属（尤其本地托管/allocated）更像一张长期保险单；它不带来 BTC 式上行，但能降低灾难上界。  
- **最短探针（30d）**：建一张“保险需求信号板”：冻结/制裁事件频率、央行/机构购金趋势、区域实物溢价、主要 ETF 流向、allocated/本地托管产品规模与交易活跃度。  
- **停机点（First Tripwire）**：规则摩擦显著下降 + 实际利率上行趋势持续（机会成本上升）；或出现黄金交易/跨境流动强限制；或所选工具出现追踪/交割异常。  
- **入口**：`distilled/core_hypotheses.md`（H-0026） / `world_understanding/xie_qinghai_gold_allocation_vault_migration_sanctions_hedge.md`

### G) 具身/VLA 知识基础设施：路线图 × 题库 × 复现清单（H-0027）

- **潜力档位**：更像 **10x（改变人生/组织效率：把“入门”变成“可交付”）**  
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：具身/VLA 的硬约束在工程交付链路；知识基础设施能显著降低 onboarding 与复现成本，并逐步变成能力标准入口。
- **最短探针（7d）**：做一次“可执行性审计”：从仓库入口出发，要求 7 天内产出 1 个可复现产物（demo/复现实验记录/小脚手架）并记录断点清单。
- **停机点（First Tripwire）**：入口缺失/信息过期导致 7 天内无法产出任何可复现产物；或维护长期失活、断链与错误无人修；或长期看不到采用/贡献闭环。
- **入口**：`distilled/core_hypotheses.md`（H-0027） / `world_understanding/vla_handbook_as_knowledge_infra_signal.md`

### H) AI 劳动力压缩：产出爆量 × 治理门槛（H-0028）

- **潜力档位**：更像 **10x（效率跃迁，但高度依赖治理）**  
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：若 AI 参与开发使“产出↑但告警/复杂度↑”，净效率将取决于审计/回归/权限治理是否到位。
- **最短探针（7d）**：做一次 AI 参与开发的回归审计：记录 AI 产出占比、静态告警/复杂度、交付周期与回滚率（写停机阈值）。
- **停机点（First Tripwire）**：告警/复杂度持续上升且交付周期无改善；或发生语义洗白导致的决策事故。
- **入口**：`distilled/core_hypotheses.md`（H-0028） / `world_understanding/ai_labor_shift_infra_bottlenecks_trust_06.md`

### I) ABB 结构：现金流/实物资产偏好（H-0029）

- **潜力档位**：更像 **1x–3x（结构轮动，不是单一资产 100x）**  
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：债券熊市 + 资本供给约束使资金偏向“真实现金流/实物资产/EM/中小盘”。
- **最短探针（30d）**：ABB 信号板：利率/利差、EM/小盘盈利、AI capex 需求 vs 信贷供给。
- **停机点（First Tripwire）**：收益率显著回落 + 信贷扩张 + 盈利改善同时成立。
- **入口**：`distilled/core_hypotheses.md`（H-0029） / `world_understanding/market_structure_abb_regime_2026_06.md`

### J) 创造力“边缘化”：品味/策展溢价（H-0030）

- **潜力档位**：更像 **3x–10x（品味层 + 策展/证明带来的溢价）**  
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：AI 把中位内容商品化，价值向“风格一致性/策展/品味证明”迁移。
- **最短探针（30d）**：品味溢价信号板：中位单价、头部溢价、风格一致性权重、付费策展占比。
- **停机点（First Tripwire）**：中位价格不降且风格溢价不升；平台推荐仍以产量/效率为主。
- **入口**：`distilled/core_hypotheses.md`（H-0030） / `world_understanding/naval_ai_creativity_learning_adaptation_2026.md`

### K) LLM 回测体检：LAP 前视偏差诊断（H-0031）

- **潜力档位**：更像 **3x（研究可信度/流程护栏，不是单一资产爆发）**  
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：LLM 预测必须先排除“记忆偷看”，否则回测收益是幻觉。
- **最短探针（30d）**：加入 LAP 诊断 + 训练截止模型样本外检验。
- **停机点（First Tripwire）**：样本外仍显著或 LAP 与预测无稳定关系。
- **入口**：`distilled/core_hypotheses.md`（H-0031） / `world_understanding/llm_finance_lap_lookahead_bias_2026.md`

### L) 算力因子重构：推理成本效率 + “管子”（互连/带宽/存储）（H-0032）

- **潜力档位**：更像 **3x–10x（结构机会，不承诺单票价格路径）**
- **当前 Gate**：**Gate 2（买信息期权）**
- **为什么值得跟踪（1 句）**：当 scale-out 规模化把瓶颈推到系统层，利润池可能从“单卡算力”迁向“推理效率 + 互连/带宽/存储”，尤其在推理侧更容易专用化。
- **最短探针（30d）**：建一张“算力瓶颈信号板”（每周 15 分钟）：推理成本趋势、瓶颈提及频次（互连/带宽/存储）、站队迹象（推理侧更明显）。
- **停机点（First Tripwire）**：一年内扩容仍主要卡单卡算力且“管子”瓶颈不再出现；推理侧专用化无可回归进展；因子重构无法解释产业/资本的边际变化。
- **入口**：`distilled/core_hypotheses.md`（H-0032） / `world_understanding/tech_2026_ai_autonomy_compute_factor_shift.md`

---

## 风险墙（永远优先：先锁灾难上界）

这些不是“机会”，但它们决定你能否活到下一次机会：

- **灰色老股/额度交易**：任何“先打款”结构 → 直接拒绝（见 `distilled/high_certainty_decisions.md` 的 D-0005）。  
- **价值捕获**：当指标开始取代意义时，必须上“意义护栏”（见 D-0007）。  

---

## 下一次更新（推荐节律）

- **每周 15 分钟**：只更新三件事：Gate、最短探针进度、第一坏信号是否出现。  
- **每月一次**：对 Top 3–5 做一次 `frameworks/06...` 的完整复跑（允许 Gate 上下移动）。  

