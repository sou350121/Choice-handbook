# Writeback Rules（Market Radar → meta/ 与 distilled/）

目标：让 Market Radar 不止“产出一份报告”，而是能推动 choice-handbook 的确定性升级：

- `sources/`：新增可回查证据快照（自动）
- `world_understanding/`：滚动雷达与 mini-06（自动）
- `distilled/`：机会图谱的 Gate/探针/停机点（半自动：脚本写 auto block）
- `meta/`：猜想的证据与下一步验证（手工：避免破坏表格）

---

## 1) 每次 run 的自动输出

运行 `run_market_radar.ps1` 或 `run_market_radar_all.ps1` 后，你会得到：

- `sources/YYYY-MM-DD_market_radar_<universe>.md`
- `world_understanding/market_radar_<universe>.md`
- `world_understanding/market_radar_runs/YYYY-MM-DD_<universe>_top3_mini06.md`
- `world_understanding/market_radar_runs/YYYY-MM-DD_<universe>_writeback.md`（回写建议）

并且（如果使用 `--writeback-opportunity-map`）会更新：
- `distilled/opportunity_map.md` 中对应 universe 的 `<!-- market_radar:auto:<universe>:... -->` 区块

---

## 2) meta 的回写（强烈建议手工）

`meta/hypotheses_registry.md` 是表格资产，自动编辑容易损坏格式与历史语义。

推荐做法（每次 run 只花 3 分钟）：打开当次的：

`world_understanding/market_radar_runs/YYYY-MM-DD_<universe>_writeback.md`

把其中 “Suggested meta updates” 的意图手工回写到对应的 `H-XXXX`：

- **核心证据（links）**：追加本次 `sources/YYYY-MM-DD_market_radar_<universe>.md`（只追加不覆写）
- **下一步验证（最小动作）**：如果本次出现了更明确的 Tripwire，就把阈值写死
- **反证信号**：如果发现旧反证太软，把它阈值化

---

## 3) distilled 的回写（脚本自动 + 你复核）

`distilled/opportunity_map.md` 的 auto block 只负责记录：
- 最新 run、evidence、mini-06 链接、Top signals

