# Case Atlas（工业自动化/机器人）— 06 硬化分册：良率×节拍×停线成本

> **定位**：这是 Case Atlas 的【工业自动化/机器人分册】（编号 `26.x` 与 `world_understanding/yearbook/README.md` 对齐）。  
> **怎么用（30 秒）**：看 `速用索引` → 选 2–3 个类比 → 只抄 **First Tripwire / Catastrophic Bound / Death Spiral** → 只留 1 条 **最短探针**。  
> **常见误区**：只看自动化率，不看良率与停线成本；只看设备，不看流程与数据闭环。  

---

## 速用索引（按“自动化系统坏信号”选类比）

- **过度自动化导致停线**：`26.1`（平衡自动化 vs 过度自动化）  
- **系统割裂缺少数据闭环**：`26.2`（标准化 MES/SCADA vs 孤岛系统）  
- **峰值产能无法提升**：`26.3`（仓储机器人 vs 人工密集）  

## 模板（固定字段，已内嵌在每条案例里）

> 每条案例都包含：Outcome / T0 / Killer Assumption / Wedge / Flywheel / First Tripwire / Catastrophic Bound / Death Spiral / Noise / 最短探针。  
> “只读一次的用法说明”见：`world_understanding/yearbook/case_atlas_financial_platform_supplychain_framework06.md`。

---

## 26.x 工业自动化/机器人（06 硬化案例）

### 26.1 平衡自动化（相对成功） vs 过度自动化（失败模式）
- **Outcome**：平衡人机协作提高良率；过度自动化在复杂工艺下停线频发。  
- **T0 环境**：产品迭代快、工艺变化频繁。  
- **Killer Assumption**：自动化越高越稳定。  
- **Wedge**：工艺变更导致设备无法快速适配。  
- **Flywheel**：稳定节拍 → 良率↑ → 成本↓ → 投资↑ → 节拍更稳。  
- **First Tripwire**：调试周期拉长、停线次数上升。  
- **Catastrophic Bound**：停线成本超过人工替代成本。  
- **Death Spiral**：停线↑ → 交付延期 → 现金流↓ → 维护投入↓ → 停线更↑。  
- **Noise**：短期单班产量提升。  
- **最短探针（7d）**：对比“自动化率提升 vs 良率变化”，若良率不升反降即判过度自动化。  

### 26.2 标准化 MES/SCADA（相对成功） vs 孤岛系统（失败模式）
- **Outcome**：标准化系统带来可视化与持续优化；孤岛系统导致故障与质量问题难闭环。  
- **T0 环境**：多工厂协同与质量追溯需求上升。  
- **Killer Assumption**：局部系统足够支撑全局优化。  
- **Wedge**：数据不可贯通，问题复发。  
- **Flywheel**：数据统一 → 追溯更快 → 良率提升 → 更愿意标准化。  
- **First Tripwire**：质量问题反复出现、跨工厂指标不一致。  
- **Catastrophic Bound**：关键批次无法追溯导致监管/客户停单。  
- **Death Spiral**：质量事故 → 追溯困难 → 客户流失 → 投入减少 → 事故更多。  
- **Noise**：单次上线成功口碑。  
- **最短探针（30d）**：统计“问题定位时间 + 批次追溯覆盖率”，低于阈值即判系统割裂。  

### 26.3 仓储机器人（相对成功） vs 人工密集（失速）
- **Outcome**：机器人提升峰值吞吐；人工密集在高峰期失效。  
- **T0 环境**：电商订单波动大、峰值压力高。  
- **Killer Assumption**：人力调度可以随时满足峰值需求。  
- **Wedge**：高峰期招聘与培训瓶颈。  
- **Flywheel**：吞吐↑ → 交付稳定 → 客户留存↑ → 投入↑ → 吞吐更高。  
- **First Tripwire**：峰值延迟增加、错误率上升。  
- **Catastrophic Bound**：高峰期 SLA 无法达标导致核心客户流失。  
- **Death Spiral**：延迟↑ → 客户流失 → 订单下降 → 投入下降 → 延迟更高。  
- **Noise**：单周人工加班产量。  
- **最短探针（48h）**：模拟峰值日订单，测“单位小时吞吐 + 错误率”，低于阈值即判不可扩张。  
