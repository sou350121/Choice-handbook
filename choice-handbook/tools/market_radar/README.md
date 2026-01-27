# Market Radar (choice-handbook)

这是一套**按需触发**的市场情报扫描工具，用来把“AI → 基础设施需求”信号落地成 choice-handbook 的可核验资产。

## What it does
- 拉取 **Futu OpenAPI（OpenD）行情**（优先）+ **Yahoo Finance 兜底**
- 拉取 **SEC EDGAR** 最近申报链接
- （可选）拉取配置的 RSS 标题
- 计算确定性的信号分数
- 产出：
  - `sources/` 的证据快照
  - `world_understanding/` 的滚动雷达
  - `world_understanding/market_radar_runs/` 的 Top-3 mini-06（US + HK/SH/SZ；强制引用 Case Atlas 的 `11.x/12.x/13.x`）

## Quick start (Windows)
1) 安装依赖
```
pip install -r choice-handbook/tools/market_radar/requirements.txt
```

2) 设置环境变量（推荐用 `.env`）
```
copy choice-handbook\tools\market_radar\.env.example choice-handbook\tools\market_radar\.env
```
填入：
- `SEC_USER_AGENT`（建议带邮箱）
- `YAHOO_USER_AGENT`（可选，用于稳定抓取）
- `FUTU_HOST` / `FUTU_PORT`（可选，默认 127.0.0.1:11111）

3) 运行
```
powershell -ExecutionPolicy Bypass -File choice-handbook\tools\market_radar\run_market_radar.ps1
```

## Outputs
- `choice-handbook/sources/YYYY-MM-DD_market_radar_<universe>.md`
- `choice-handbook/world_understanding/market_radar_<universe>.md`
- `choice-handbook/world_understanding/market_radar_runs/YYYY-MM-DD_<universe>_top3_mini06.md`

## Extend watchlist
编辑：`choice-handbook/tools/market_radar/config/watchlist.yaml`

字段：
- `symbol`: 代码（美股通用）
- `futu_code`: Futu 代码（如 `HK.00700` / `SH.600900` / `SZ.000001`，可选）
- `name`: 公司名
- `tags`: [memory, compute, network, power, cooling, server, ...]
- `rss`: 可选 RSS 列表（默认空）

数据源选择：
- `primary_provider`: `futu` 或 `yahoo`
- `fallback_provider`: `yahoo`（默认）

## Notes
- 本工具**不自动交易**，只产出证据与 mini-06。
- 若要完整 06，请用 `frameworks/06_time_travel_endgame_simulator.md`。
- 回写规则（让雷达真正推动确定性升级）：`choice-handbook/tools/market_radar/WRITEBACK.md`。

## Run with topic configs (recommended)
你可以通过 `--config` 指定不同主题的信号板（universe），把“都要”拆成可扩展模块：```powershell
# AI Infra 瓶颈迁移（覆盖内存/显存类爆炸）
python -m market_radar.run --root d:\Project_dev\choice-handbook --config tools/market_radar/config/topics/aiinfra_bottleneck_shift.yaml

# 模型价格战 → 盈利池迁移（SoR/数据围墙/分发）
python -m market_radar.run --root d:\Project_dev\choice-handbook --config tools/market_radar/config/topics/model_price_war_profit_pool_shift.yaml
```

信号板规范见：`choice-handbook/tools/market_radar/SIGNAL_BOARD_SPEC.md`。
