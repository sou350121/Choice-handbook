# Clawdbot GitHub Repo Snapshot（证据快照）

> Snapshot date：2026-01-27  
> Repo：`https://github.com/clawdbot/clawdbot`  
> 说明：本文件只记录“当日可核验的一手信息”（避免把二手传播当事实）。

---

## 1) Repo 基本信息（可回查）

- **URL**：`https://github.com/clawdbot/clawdbot`
- **License**：MIT（见 `https://raw.githubusercontent.com/clawdbot/clawdbot/main/LICENSE`）
- **Stars / Forks（按 2026-01-27 抓取）**：56,850 stars / 6.8k forks  
  - 来源：GitHub 仓库页（Snapshot 抓取于 2026-01-27）

---

## 2) 项目一句话（README 可核验）

- “Personal AI assistant you run on your own devices.”（本地运行的个人 AI 助手）
- **多渠道入口**：WhatsApp / Telegram / Slack / Discord / Google Chat / Signal / iMessage / Microsoft Teams / WebChat 等（以及扩展通道）。
- **核心结构**：Gateway 是控制平面（control plane）；“产品是 assistant 本身”。

---

## 3) 运行入口 / 安装方式（README 可核验）

- **Runtime**：Node ≥ 22
- **推荐安装（npm/pnpm）**：

```bash
npm install -g clawdbot@latest
clawdbot onboard --install-daemon
```

- **启动 Gateway（示例）**：

```bash
clawdbot gateway --port 18789 --verbose
```

- **从源代码开发（pnpm）**：
  - `pnpm install`
  - `pnpm ui:build`
  - `pnpm build`
  - `pnpm gateway:watch`（TS 变更自动 reload）

---

## 4) 架构骨架（README 可核验）

### 4.1 “How it works (short)”（README 图）

- 多个聊天/入口通道 → **Gateway（WS control plane）** → agent runtime / CLI / WebChat UI / macOS app / iOS/Android nodes
- Gateway 默认绑定 loopback（`ws://127.0.0.1:18789`）

### 4.2 关键子系统（README 列表）

- Gateway WebSocket 控制平面（sessions/presence/config/cron/webhooks）
- 可选远程暴露：Tailscale Serve/Funnel 或 SSH tunnels（强调 auth）
- 工具：browser control（CDP）、nodes（camera/screen/location/system.run 等）、skills 平台

---

## 5) 安全与默认策略（README 可核验）

### 5.1 DM 默认不信任（pairing）

- “Treat inbound DMs as untrusted input.”  
- 默认 DM pairing：未知发送者不会被处理，需要 pairing approve 才加入 allowlist

### 5.2 Sandbox（非 main 会话）

- 通过 `agents.defaults.sandbox.mode: "non-main"` 把非 main session 放入 per-session Docker sandbox
- Sandbox allowlist/denylist：默认仅允许部分工具；可禁用 browser/canvas/nodes 等高危能力

---

## 6) 与本文档体系的 Delta（对既有分析的影响）

这份 snapshot 对 `choice-handbook` 的影响主要在 3 点（把不确定性收敛到可执行门禁）：

1) **“桌面 Cowork/执行权”不是概念**：Clawdbot 的 Gateway/control-plane/多通道结构与默认安全策略，提供了可核验的“形态样本”。  
2) **安全门槛被产品化**：pairing、allowlist、sandbox、doctor（风险检查）说明“执行器”必须内置治理，否则灾难上界不可控。  
3) **分发/采用的关键摩擦**：Node≥22、daemon、通道接入与权限（尤其 macOS 权限/TCC）是落地现实约束，决定“能否规模化”。

