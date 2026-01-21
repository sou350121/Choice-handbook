# 猜想/主张注册表（Hypotheses Registry）

> 目标：把“文章里的推演/猜想”变成可追踪资产：**能被新证据验证/反证**，并推动更高确定性的决策。

## 状态与置信度（建议）

- **状态**：`open`｜`weakly_supported`｜`supported`｜`validated`｜`invalidated`
- **置信度**：20% / 50% / 80%（见 `frameworks/05_reasoning_toolkit.md` 的 `C2.4`）

## 登记规则（强制）

- **每条猜想必须可证伪**：写清楚“什么证据出现就算我错了”
- **每条猜想必须可更新**：写清楚“观察信号”与“下一步验证”
- **每条猜想必须有出处**：至少链接到首次提出它的文档（通常是 `world_understanding/*.md`）

---

## Registry（请保持短而密）

| ID | 猜想（可证伪陈述） | 首次提出（link） | 当前状态 | 置信度 | 核心证据（links，按时间追加） | 反证信号（出现就降级） | 下一步验证（最小动作） | 最后更新 |
|---|---|---|---|---|---|---|---|---|
| H-0001 | 可规模化训练里，“可保证的稳定性约束”会逐步成为默认（而不是靠调参碰运气）；逐层稳定性指标会进入标配监控 | `world_understanding/mhc_manifold_hyperconnections_residual_conservation.md` | supported | 80% | `sources/2026-01-19_deepseek_mhc_reproduction_kolasinski.md` / `world_understanding/mhc_manifold_hyperconnections_residual_conservation.md` | 大规模训练中，无约束混合长期稳定且无 Amax 漂移；约束层收益无法复现 | 选一条训练栈：加逐层 Amax + layer0 canary + 压力测试阈值 | 2026-01-20 |
| H-0002 | AI 供应链的“交付瓶颈”会在一段时间内从制程迁移到封装/产能/认证链条；瓶颈会驱动订单外溢与第二路线窗口 | `world_understanding/tsmc_cycle_philosophy_cowos_emib.md` | supported | 80% | `sources/2026-01-19_tsmc_cycle_philosophy_cowos_emib.md` / `world_understanding/tsmc_cycle_philosophy_cowos_emib.md` | 交期/报价显著回落且长期稳定；外溢无法持续且第二路线里程碑不可回归 | 把“兑现链条五段”写成每月信号板（交期/良率/认证/报价/外溢） | 2026-01-20 |
| H-0003 | LLM/Agent 的真实进步会从“榜单/刷榜”迁移到“真实任务回归集 + 对抗集 + 权限/审计治理”，否则不可持续 | `world_understanding/state_of_llms_2025_raschka.md` | supported | 80% | `sources/2026-01-19_raschka_state_of_llms_2025.md` / `sources/2026-01-19_karpathy_llm_year_in_review_2025.md` | 榜单提升能稳定转化为真实任务成功率提升且无额外安全/成本问题 | 做一个 10–30 条真实任务回归集 + 3–5 条对抗集 + 最小权限 allowlist | 2026-01-20 |
| H-0004 | 具身/机器人里，“数据质量”的主要瓶颈不是更干净，而是更高信号密度（关键窗口/失败恢复/覆盖/对齐）+ 可检索可版本化的数据基础设施 | `world_understanding/robotics_data_infrastructure.md` | supported | 80% | `sources/2026-01-19_ken_goldberg_robotics_data_infrastructure.md` / `sources/2026-01-19_gaoyang_spirit_v1_5_clean_data_enemy.md` / `world_understanding/embodied_openai_playbook_wang_qian.md` | 更 clean 的流程在迁移/恢复上持续胜出，且组织成本不线性增长 | 先做关键窗口切片 + 失败分类 + 回归集 + 检索/版本化最小管道 | 2026-01-20 |
| H-0005 | 灵巧手/家务级操纵的真正门槛是“接近 100% 的成功率 + 可恢复性 + 触觉/力控”，demo 成功率不等于可交付 | `world_understanding/dexterous_hands_hardware_algorithms.md` | supported | 80% | `sources/2026-01-19_dexterous_hands_hardware_algorithms_silicon101.md` / `world_understanding/dexterous_hands_hardware_algorithms.md` | 在无触觉/弱回归下仍可跨任务稳定逼近可交付门槛；维护/装配成本不随规模爆炸 | 选 1 个任务做 20+ 次回归：成功率+恢复率+失败分类，并写停机阈值 | 2026-01-20 |
| H-0006 | 注意力是生活“实际货币”；改系统默认入口（触发器/配额/深度块）比靠意志力更有效，并能带来稳定产出提升 | `world_understanding/attention_is_currency_of_life_naval.md` | supported | 80% | `sources/2026-01-20_naval_attention_currency_of_life.md` / `sources/2026-01-20_naval_observe_mind_loops_holistic_selfishness.md` / `world_understanding/attention_is_currency_of_life_naval.md` / `world_understanding/observe_mind_loops_holistic_selfishness_naval.md` | 降触发器/设深度块对产出与在场感无改善（连续 2–4 周） | 做 7 天注意力预算试运行：配额+3个深度块+记录（输入/切换/输出） | 2026-01-20 |
| H-0007 | 自动化交易/实时系统存在“聪明 vs 快”的硬 Pareto：延迟预算会吞噬 alpha，模型选择必须先满足延迟与滑点硬约束 | `world_understanding/foundation_models_automated_trading_hrt_hail.md` | supported | 50% | `sources/2026-01-19_hrt_hail_foundation_models_automated_trading_icml_2025.md` / `world_understanding/foundation_models_automated_trading_hrt_hail.md` | 更慢更聪明模型在固定延迟预算下仍稳定净胜，并跨 regime 可回归 | 同一指标板画 3 点（快/慢/混合），并做 time-vs-event tokenization A/B | 2026-01-20 |
| H-0008 | “产能=时间窗口”的资本结构动作（预付款/参建/并购）会在供给紧约束期反复出现，并把超额收益重新分配给能兑现五段链条者 | `world_understanding/capacity_sovereignty_era.md` | supported | 50% | `world_understanding/capacity_sovereignty_era.md` | 交期缩短、预付款退潮、溢价收敛且持续；五段兑现不再是瓶颈 | 选一个具体案例，按五段链条做证据与信号板（每段 2 信号） | 2026-01-20 |
| H-0009 | “窗口期（上市/规则）”会把产业兑现前置定价：在兑现链条未验证前，财富效应与板块情绪先发生，同时灰色老股/额度交易与骗局会增多 | `world_understanding/commercial_space_ipo_window_wealth_effect.md` | supported | 50% | `sources/2026-01-20_commercial_space_first_wave_wealth_effect_ipo_wave_china.md` / `world_understanding/commercial_space_ipo_window_wealth_effect.md` | 窗口期并未引发情绪与提前定价；或市场对“先打款”结构普遍拒绝且骗局不再高发 | 建一个“兑现信号板”，跟踪：IPO 进度/交付/订单/现金流/情绪，并记录灰色交易出现频率 | 2026-01-20 |
| H-0010 | 当宏观风险“难以定价”且离散度上升时，Alpha（多空/事件/相对价值）相对 Beta（方向性押注）的性价比会显著上升；尾部风险自满会周期性创造长波动机会 | `world_understanding/unpriceable_markets_dispersion_alpha_window_man_group.md` | supported | 50% | `sources/2026-01-20_man_group_2026q1_unpriceable_markets_alpha_window.md` / `world_understanding/unpriceable_markets_dispersion_alpha_window_man_group.md` | 离散度不升反降、相关性持续走高；或方向性 Beta 在同等风险下长期稳定压倒 Alpha | 建一个“Alpha 环境仪表盘”（相关性/离散度、M&A、曲线、波动率期限结构、拥挤度）并按月复盘 | 2026-01-20 |
| H-0011 | 任何长期运行的评分系统都会发生“价值捕获”：代理指标会取代真实价值，导致表演式优化与意义扁平化；除非系统引入反扭曲机制（质性复盘/对抗样本/审计），否则会持续走偏 | `world_understanding/value_capture_play_the_right_game.md` | supported | 50% | `sources/2026-01-21_value_capture_scores_replace_meaning_c_thi_nguyen.md` / `world_understanding/value_capture_play_the_right_game.md` | 指标上升长期稳定带来真实价值上升，且投机空间极低；或反扭曲机制并不影响刷分行为但仍能保持意义 | 做一次“反 Goodhart 审计”：列 3 条刷分路径 + 为每条加一个阻断，并在 2–4 周后复盘结果 | 2026-01-21 |
| H-0012 | 孤独/弱连接是结构性趋势：当连接稀缺时，“感觉被商业化”（安定/连接/共创/慰藉/独特）会成为长期需求；单点玩梗产品只能短期爆火，长期赢家来自服务链条与真实响应 | `world_understanding/loneliness_economy_five_feelings.md` | supported | 50% | `sources/2026-01-21_loneliness_economy_sileme_app.md` / `world_understanding/loneliness_economy_five_feelings.md` | 独居与弱连接趋势被显著逆转；或用户不再为“感觉”付费且公共服务/社区网络低成本替代 | 做“连接资产表”并跟踪 4 周：可响应度/共创频率/情绪通道成本是否下降 | 2026-01-21 |
| H-0013 | AI 应用层长期赢家更可能收敛为“系统记录（SoR）+ 工作流中枢 + 围墙花园数据（独家授权/采集网络/闭环结果数据）”；薄工具/薄包装会被模型同质化与平台下沉挤压 | `world_understanding/a16z_ai_investment_logic_three_paths_rampell.md` | supported | 80% | `sources/2026-01-21_a16z_ai_investment_logic_three_paths_rampell.md` / `world_understanding/a16z_ai_investment_logic_three_paths_rampell.md` | 在缺少 SoR/数据围墙的情况下，薄工具仍能长期维持定价权与高留存（跨周期成立）；或平台下沉不影响其利润池 | 用一张“护城河打分卡”对 3 个候选做验证：SoR 证据、闭环结果数据、定价从 seat→usage/outcome 的迁移是否可回归（4–8 周） | 2026-01-21 |

> 说明：ID 不要变更；证据只追加不覆写（用最新证据改变状态/置信度）。

