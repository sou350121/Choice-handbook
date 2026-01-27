# Case Atlas（网络安全/信任/身份）— 06 硬化分册：攻击面×权限×恢复力

> **定位**：这是 Case Atlas 的【网络安全/信任/身份分册】（编号 `18.x` 与 `world_understanding/yearbook/README.md` 对齐）。  
> **怎么用（30 秒）**：看 `速用索引` → 选 2–3 个类比 → 只抄 **First Tripwire / Catastrophic Bound / Death Spiral** → 只留 1 条 **最短探针**。  
> **常见误区**：只看合规，不看攻击面与恢复力；只看检测，不看权限隔离与可回滚。  

---

## 速用索引（按“安全系统坏信号”选类比）

- **端点/检测能力落后**：`18.1`（云原生 EDR vs 传统杀毒）  
- **边界模型失效（VPN/内网过信任）**：`18.2`（Zero Trust vs Perimeter）  
- **供应链/构建系统被渗透**：`18.3`（SolarWinds vs 可信构建）  

## 模板（固定字段，已内嵌在每条案例里）

> 每条案例都包含：Outcome / T0 / Killer Assumption / Wedge / Flywheel / First Tripwire / Catastrophic Bound / Death Spiral / Noise / 最短探针。  
> “只读一次的用法说明”见：`world_understanding/yearbook/case_atlas_financial_platform_supplychain_framework06.md`。

---

## 18.x 网络安全/信任/身份（06 硬化案例）

### 18.1 云原生 EDR（相对成功） vs 传统杀毒（失速）
- **Outcome**：云原生检测与响应能力更能应对新型攻击；传统签名杀毒在复杂攻击下失效。  
- **T0 环境**：终端与云混合，攻击手法快速演化。  
- **Killer Assumption**：签名与周期性更新足以覆盖新威胁。  
- **Wedge**：攻击手法变形与横向移动增加。  
- **Flywheel**：检测能力↑ → 响应速度↑ → 侵害成本↑ → 攻击效率↓ → 风险降低。  
- **First Tripwire**：高危事件滞后发现、误报/漏报率上升。  
- **Catastrophic Bound**：无法在 24–48h 内发现横向扩散。  
- **Death Spiral**：检测滞后 → 侵害扩大 → 修复成本↑ → 预算被挤压 → 检测更弱。  
- **Noise**：短期合规通过与供应商宣传。  
- **最短探针（7d）**：做一次红队演练，测“发现时间 + 横向移动阻断率”。  

### 18.2 Zero Trust（相对成功） vs Perimeter/VPN（失败模式）
- **Outcome**：零信任以最小权限与持续验证降低入侵扩散；过度信任内网导致单点突破全盘失守。  
- **T0 环境**：远程办公与多云普及，传统边界模糊。  
- **Killer Assumption**：只要边界守住，内部就安全。  
- **Wedge**：凭证泄露与社工攻击绕过边界。  
- **Flywheel**：最小权限 → 横向移动难 → 损失可控 → 安全信任提升 → 更强管控。  
- **First Tripwire**：特权账号过多、VPN 依赖过高、异常横向访问频繁。  
- **Catastrophic Bound**：单个账号可访问关键资产，且无细粒度隔离。  
- **Death Spiral**：边界被破 → 横向扩散 → 核心资产失守 → 信任崩 → 更难恢复。  
- **Noise**：短期“加强密码策略”的表面措施。  
- **最短探针（48h）**：列“关键资产到特权账号”的最短路径，若路径<阈值即视为高危。  

### 18.3 SolarWinds（失败） vs 可信构建/供应链治理（相对成功）
- **Outcome**：构建链被植入后门导致大规模供应链入侵；可信构建能显著降低此类风险。  
- **T0 环境**：软件供应链复杂，依赖大量第三方组件。  
- **Killer Assumption**：供应链与构建系统本身可信，不会成为攻击入口。  
- **Wedge**：构建流水线被渗透、签名与发布被滥用。  
- **Flywheel**：供应链攻击成功 → 信任下降 → 客户流失 → 安全投入受限 → 更易被攻击。  
- **First Tripwire**：构建环境权限过大、依赖未锁定、审计链条不完整。  
- **Catastrophic Bound**：发布签名被滥用或构建系统失控。  
- **Death Spiral**：供应链受损 → 客户撤离 → 收入下降 → 安全预算压缩 → 更大风险。  
- **Noise**：短期“补丁发布”与公开声明。  
- **最短探针（30d）**：要求“可重复构建 + SBOM + 关键依赖锁定”，任一缺失即判高危。  
