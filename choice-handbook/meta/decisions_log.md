# 决策日志（Decisions Log）

> 目标：把“高确定性建议”写成可复盘条目：**证据链** + **置信度** + **退出/重启条件**，并能随新材料更新。

## 记录规则（强制）

- 只有当建议能落到“可执行 + 可退出”时，才允许写成强建议（强烈推荐/强烈不推荐）
- 每条决策必须绑定至少 1 条 `H-XXXX` 猜想，并反向链接到证据材料
- 每条决策必须有“退出条件 + 重启条件”（默认可随证据更新）

---

## Log

| ID | 决策（强建议/不建议） | 置信度 | 绑定猜想 | 关键证据（links） | 退出条件（可观测） | 重启条件（可观测） | 最近复盘 |
|---|---|---:|---|---|---|---|---|
| D-0001 | 任何 LLM/Agent 落地：**强烈推荐先做“真实任务回归集 + 最小权限/审计/停机”**，再谈刷榜/堆模型 | 80% | H-0003 | `world_understanding/state_of_llms_2025_raschka.md` / `world_understanding/llm_year_in_review_2025_karpathy.md` | 连续 2–4 周回归集无改善且主要问题不是权限/评测缺失 | 回归集/对抗集可稳定回归，且权限事故为 0 或低于阈值 | 2026-01-20 |
| D-0002 | 新架构/训练规模化：**强烈推荐把稳定性当硬约束（逐层监控 + 压力测试 + 停机阈值）**，避免“loss 正常但内部爆炸” | 80% | H-0001 | `world_understanding/mhc_manifold_hyperconnections_residual_conservation.md` | layer0/逐层 Amax 趋势持续上升并越过内部阈值（如 >10）且无法逆转 | Amax 回到接近 1.0，跨 seed 方差显著下降，压力测试通过 | 2026-01-20 |
| D-0003 | 具身/机器人路线：**强烈推荐先把系统跑起来（可测 baseline + 数据管道可检索可版本化 + 关键窗口/失败分类回归）**，再押更激进端到端 | 80% | H-0004 | `world_understanding/robotics_data_infrastructure.md` / `world_understanding/embodied_data_clean_vs_diverse_spirit_v1_5.md` / `world_understanding/embodied_openai_playbook_wang_qian.md` | 关键窗口成功率/恢复率连续 N 次迭代无提升，且数据无法归因/检索/对齐 | 回归集建立且指标可回归；数据系统可版本化；迁移成本下降 | 2026-01-20 |
| D-0004 | 个人选择（注意力）：**强烈推荐做“注意力预算”并改默认入口**（配额+深度块+记录），把输入转成输出 | 80% | H-0006 | `world_understanding/attention_is_currency_of_life_naval.md` / `world_understanding/observe_mind_loops_holistic_selfishness_naval.md` | 连续 2–4 周深度块≈0 且主要来自可控触发器；输出不增长 | 触发器明显下降，且每周稳定产出 1–3 个可交付成果 | 2026-01-20 |
| D-0005 | 灰色老股/额度交易：**强烈不推荐任何“先打款再签协议/无托管无对价保障”的老股或 LP 额度**（这不是投资，是对手方风险赌局） | 80% | H-0009 | `world_understanding/commercial_space_ipo_window_wealth_effect.md` | 你无法获得托管/可执行合同/清晰交割路径；或对方要求先打款 | 资金通过托管/律师监管账户；合同可执行；交割路径清晰且可复盘 | 2026-01-20 |
| D-0006 | 投资/资产配置：在“难以定价 + 高离散度”环境下，**强烈推荐少做单一方向押注，优先用可对冲 Beta 的 Alpha 策略（多空/事件/相对价值）+ 明确风控阈值** | 80% | H-0010 | `world_understanding/unpriceable_markets_dispersion_alpha_window_man_group.md` | 离散度下降且相关性上升，Alpha 机会集枯竭；或策略拥挤导致回撤超阈值 | 离散度/事件回归、策略可稳定回归且回撤受控 | 2026-01-20 |
| D-0007 | 个人/组织的指标治理：**强烈推荐建立“意义护栏”，把分数永远降级为工具**（防止价值捕获/表演式优化） | 80% | H-0011 | `world_understanding/value_capture_play_the_right_game.md` | 你发现自己/团队开始“为了分数而活”，出现刷分路径（投机/作弊/表演式工作）且真实价值下降 | 加入质性复盘/对抗样本/审计后，刷分路径被封堵，且真实价值指标（作品/关系/学习/客户问题解决）回升 | 2026-01-21 |
| D-0008 | 个人系统：把孤独当结构性风险，**强烈推荐做“连接资产配置”而不是只消费慰藉**（安定/连接/共创/情绪通道） | 80% | H-0012 | `world_understanding/loneliness_economy_five_feelings.md` | 你持续用消费替代连接（刷内容/买陪伴）但可响应联系人仍为 0；或情绪通道仍高成本、羞耻、不可持续 | 你有 ≥3 个可响应联系人 + 每周 1 次共创任务 + 情绪通道低成本可用 | 2026-01-21 |
| D-0009 | AI 投资/下注：**强烈推荐优先选择“系统记录（SoR）+ 围墙花园数据/结果闭环”的公司形态，谨慎对待薄工具/薄包装** | 80% | H-0013 | `world_understanding/a16z_ai_investment_logic_three_paths_rampell.md` | 同类功能竞争加剧后，目标公司留存与定价权持续下滑且不可逆；或关键数据授权不稳/同业可得；或无法进入关键交付/审计路径（SoR 失败） | 出现可回归的 SoR 证据（迁移成本上升、进入交付与审计）；闭环结果数据持续产生并带来可回归提升；定价从 seat→usage/outcome 的迁移可持续 | 2026-01-21 |
| D-0010 | 资产配置：**强烈推荐把贵金属当“退出权/保险层”**（而不是复利资产） | 80% | H-0026 | `world_understanding/xie_qinghai_gold_allocation_vault_migration_sanctions_hedge.md` | 实际利率长期上行（机会成本显著上升）且规则摩擦显著下降（保险需求退潮）；或出现贵金属交易/跨境流动强限制；或工具出现追踪/交割异常 | 冻结/制裁风险再升温；或区域实物溢价/央行购金等“保险需求信号”重新抬头；且所选工具层风险可控 | 2026-01-22 |
| D-0011 | 具身/VLA 学习与团队培养：**强烈推荐先用“知识基础设施”把新人变成可交付者** | 80% | H-0027 | `world_understanding/vla_handbook_as_knowledge_infra_signal.md` / `sources/2026-01-21_vla_handbook_github_repo.md` | 7 天内无法产出任何可复现产物（且原因主要是入口缺失/信息过期）；或维护长期失活导致无法稳定迭代 | 出现稳定可执行入口（脚手架/复现清单/回归点），且能在 2–8 周内持续产出可回归交付物 | 2026-01-22 |

