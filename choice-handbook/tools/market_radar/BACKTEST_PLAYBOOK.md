# Backtest / Replay Playbook（验证“能否提前预视”）

目标：不追求数据完美，而是验证“流程是否能提前进入 Warning / Tripwire 是否会触发 / 是否能靠退出阈值避免追涨叙事”。

> 说明：当前 replay 只对 Yahoo 数据做“as-of 回放”（通过 `--run-date` 截断历史窗口）。Futu/SEC/RSS 仍以实时为主。

---

## 1) 回放的基本命令

```powershell
# 以 2025-12-15 为“当时”，回放 aiinfra_bottleneck_shift
python -m market_radar.run --root d:\Project_dev\choice-handbook --run-date 2025-12-15 --config tools/market_radar/config/topics/aiinfra_bottleneck_shift.yaml
```

你会得到：
- `sources/2025-12-15_market_radar_aiinfra_bottleneck_shift.md`
- `world_understanding/market_radar_aiinfra_bottleneck_shift.md`
- `world_understanding/market_radar_runs/2025-12-15_aiinfra_bottleneck_shift_top3_mini06.md`
- `world_understanding/market_radar_runs/2025-12-15_aiinfra_bottleneck_shift_writeback.md`

---

## 2) 怎么判定“提前看见了”

对每个事件，做 3 个时间点（至少 3 次 run）：

- **T-8w**：事件前 8 周
- **T-2w**：事件前 2 周
- **T+2w**：事件后 2 周（验证是否应退出/降级）

你只看三件事：
- **是否进入 Warning**：score 是否显著抬升、bucket 是否稳定（memory/supplychain/platform/financial）
- **Tripwire 是否变硬**：mini-06 里的 Tripwire 是否能写成阈值化信号（而不是空话）
- **退出是否可执行**：当事件兑现后，你是否有明确退出/重启阈值（避免追涨叙事）

---

## 3) 推荐的 3 个“回放事件”样板（你可替换）

### A) 内存/显存链条的“价格爆炸/紧约束”阶段
- universe：`aiinfra_bottleneck_shift`
- 观察：`MU` 这类 memory 标签是否在事件前进入 Top3、是否稳定落在 `memory` bucket
- 你要的不是“预测价格”，而是提前看到：**供给紧约束开始形成**，并把它写成 Tripwire/Bound。

### B) AI Infra 瓶颈迁移：网络/电力/散热成为主矛盾
- universe：`aiinfra_bottleneck_shift` 或 `us_ai_infra`
- 观察：`VRT/ETN/PWR/ANET/AVGO` 等是否在某段时间持续进入 Top3
- 目标：提前识别“GPU 不是唯一瓶颈”，并把探针从“看新闻”升级为“信号板”。

### C) 平台/SoR 的盈利池迁移（模型价格战后的结构赢家）
- universe：`model_price_war_profit_pool_shift`
- 观察：bucket 是否稳定落在 `platform` / `financial`（取决于当时市场压力）
- 目标：把“叙事”变成可验证：SoR 证据、数据围墙证据、定价权证据。

---

## 4) 失败也有价值：怎么复盘

如果回放发现：\n
- score 总是很低、Top3 很随机：说明信号板太弱（需要引入更接近产业硬约束的信号：交期/报价/库存/Capex/bit growth）。\n
- Tripwire 仍是空话：说明你需要把“阈值写死”前移到 signal board（别让 mini-06 兜底）。\n
- 事件后仍不退出：说明你把 Bound 写成了情绪，而不是可观测阈值。\n

