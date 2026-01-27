# Case Atlas（数据/可观测性/DevOps）— 06 硬化分册：可靠性×效率×标准化

> **定位**：这是 Case Atlas 的【数据/可观测性/DevOps 分册】（编号 `29.x` 与 `world_understanding/yearbook/README.md` 对齐）。  
> **怎么用（30 秒）**：看 `速用索引` → 选 2–3 个类比 → 只抄 **First Tripwire / Catastrophic Bound / Death Spiral** → 只留 1 条 **最短探针**。  
> **常见误区**：只看工具数量，不看可观测性闭环；只看迁移成本，不看效率收益。  

---

## 速用索引（按“数据/运维坏信号”选类比）

- **监控工具拼盘、排障效率低**：`29.1`（统一可观测平台 vs 工具拼盘）  
- **数据平台性能/成本失控**：`29.2`（云数仓 vs 本地数仓）  
- **发布效率与稳定性冲突**：`29.3`（CI/CD 自动化 vs 手工发布）  

## 模板（固定字段，已内嵌在每条案例里）

> 每条案例都包含：Outcome / T0 / Killer Assumption / Wedge / Flywheel / First Tripwire / Catastrophic Bound / Death Spiral / Noise / 最短探针。  
> “只读一次的用法说明”见：`world_understanding/yearbook/case_atlas_financial_platform_supplychain_framework06.md`。

---

## 29.x 数据/可观测性/DevOps（06 硬化案例）

### 29.1 统一可观测平台（相对成功） vs 工具拼盘（失败模式）
- **Outcome**：统一平台提升排障效率；工具拼盘导致盲区与误判。  
- **T0 环境**：微服务扩展，系统复杂度上升。  
- **Killer Assumption**：多个独立工具加起来就等于整体可观测性。  
- **Wedge**：指标/日志/追踪割裂导致排障缓慢。  
- **Flywheel**：可观测性↑ → MTTR↓ → 可靠性↑ → 投入↑ → 可观测性更好。  
- **First Tripwire**：排障时间上升、重复事故频发。  
- **Catastrophic Bound**：关键故障无法在 SLA 内定位与恢复。  
- **Death Spiral**：事故↑ → 信任↓ → 预算↓ → 监控更差 → 事故更多。  
- **Noise**：单次“救火”成功。  
- **最短探针（7d）**：测“MTTR + 事故复发率”，高于阈值即判可观测性不足。  

### 29.2 云数仓（相对成功） vs 本地数仓（失速）
- **Outcome**：云数仓弹性扩展与成本可控；本地数仓在负载与维护上失速。  
- **T0 环境**：数据规模增长、团队需求多样化。  
- **Killer Assumption**：本地数仓升级可以持续跟上需求。  
- **Wedge**：扩容周期长与维护成本上升。  
- **Flywheel**：弹性能力↑ → 使用场景↑ → 价值↑ → 投入↑ → 弹性更强。  
- **First Tripwire**：查询排队时间上升、维护窗口频繁。  
- **Catastrophic Bound**：扩容成本与停机时间无法接受。  
- **Death Spiral**：性能差 → 使用减少 → 投入下降 → 性能更差。  
- **Noise**：短期成本上涨或迁移舆论。  
- **最短探针（30d）**：统计“峰值负载与扩容周期”，超过阈值即判本地模式失速。  

### 29.3 CI/CD 自动化（相对成功） vs 手工发布（失败模式）
- **Outcome**：自动化降低发布风险与频率成本；手工发布在复杂系统中失败。  
- **T0 环境**：迭代节奏加快，发布频率上升。  
- **Killer Assumption**：手工流程可在规模化下维持质量。  
- **Wedge**：人为错误与回滚成本上升。  
- **Flywheel**：自动化↑ → 发布频率↑ → 反馈更快 → 质量更高 → 自动化更强。  
- **First Tripwire**：发布失败率上升、回滚频繁。  
- **Catastrophic Bound**：重大事故导致长时间停机与信任损失。  
- **Death Spiral**：失败↑ → 发布冻结 → 积压↑ → 风险更高 → 失败更大。  
- **Noise**：单次发布顺利。  
- **最短探针（48h）**：测“发布失败率 + 回滚时间”，高于阈值即判流程不可扩张。  
