# Case Atlas（资本市场/交易所/清算）— 06 硬化分册：流动性×清算×规则风险

> **定位**：这是 Case Atlas 的【资本市场/交易所/清算分册】（编号 `27.x` 与 `world_understanding/yearbook/README.md` 对齐）。  
> **怎么用（30 秒）**：看 `速用索引` → 选 2–3 个类比 → 只抄 **First Tripwire / Catastrophic Bound / Death Spiral** → 只留 1 条 **最短探针**。  
> **常见误区**：只看成交量，不看清算与对手方风险；只看规则，不看极端情景下的规则变更。  

---

## 速用索引（按“市场结构坏信号”选类比）

- **人工/离散市场被电子化替代**：`27.1`（电子撮合 vs 场内）  
- **双边 OTC 风险不可控**：`27.2`（中央清算 vs 双边）  
- **极端波动时风控失效**：`27.3`（实时风控 vs 无硬阈值）  

## 模板（固定字段，已内嵌在每条案例里）

> 每条案例都包含：Outcome / T0 / Killer Assumption / Wedge / Flywheel / First Tripwire / Catastrophic Bound / Death Spiral / Noise / 最短探针。  
> “只读一次的用法说明”见：`world_understanding/yearbook/case_atlas_financial_platform_supplychain_framework06.md`。

---

## 27.x 资本市场/交易所/清算（06 硬化案例）

### 27.1 电子撮合交易所（成功） vs 场内人工撮合（失速）
- **Outcome**：电子撮合降低成本与滑点；场内人工在效率与透明度上失速。  
- **T0 环境**：技术成熟与延迟敏感交易增长。  
- **Killer Assumption**：人工撮合能长期提供更好的流动性与价格发现。  
- **Wedge**：成本与速度优势形成迁移。  
- **Flywheel**：流动性↑ → 点差↓ → 交易量↑ → 流动性更高。  
- **First Tripwire**：点差扩大、交易量迁移到电子平台。  
- **Catastrophic Bound**：主要产品流动性完全转移。  
- **Death Spiral**：流动性↓ → 点差↑ → 交易量↓ → 流动性更↓。  
- **Noise**：单次大宗交易或短期波动。  
- **最短探针（30d）**：看“主力合约成交量占比”，低于阈值即判迁移完成。  

### 27.2 中央清算（相对成功） vs 双边 OTC（失败模式）
- **Outcome**：中央清算降低对手方风险；双边 OTC 在危机中传染。  
- **T0 环境**：衍生品规模大、网络化对手方高度复杂。  
- **Killer Assumption**：对手方信用在极端下仍可控。  
- **Wedge**：违约与保证金缺口传染。  
- **Flywheel**：清算集中 → 风险可见 → 保证金合理 → 信任↑ → 更多清算。  
- **First Tripwire**：双边保证金争议、违约传染迹象。  
- **Catastrophic Bound**：关键对手方违约引发链式清算失败。  
- **Death Spiral**：违约 → 信用收缩 → 保证金上升 → 流动性枯竭 → 更大违约。  
- **Noise**：短期“市场稳定”表述。  
- **最短探针（48h）**：测“集中对手方暴露 + 保证金缺口”，超过阈值即判系统性风险。  

### 27.3 实时风控与限仓（相对成功） vs 无硬阈值（失败模式）
- **Outcome**：实时限仓限制极端波动；缺乏硬阈值易出现闪崩与操纵。  
- **T0 环境**：算法交易占比高、市场反应快。  
- **Killer Assumption**：市场会自我纠偏，不需硬阈值。  
- **Wedge**：流动性瞬间蒸发。  
- **Flywheel**：风控有效 → 信心↑ → 流动性↑ → 风控更有效。  
- **First Tripwire**：订单簿变薄、撮合失败频发。  
- **Catastrophic Bound**：单边波动触发系统性停市或失序。  
- **Death Spiral**：波动↑ → 流动性↓ → 更大滑点 → 波动更↑。  
- **Noise**：短期价格回归。  
- **最短探针（7d）**：监测“订单簿深度 + 滑点分布”，低于阈值即判风控不足。  
