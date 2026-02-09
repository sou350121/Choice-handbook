# Choice Handbook（选择手册）

> 极限的思索，是把自己推到边界：看见“本来可以发生的”，也看见“为何没发生”。  
> 尽头常在远方，有时候却是现实——它不是终点，而是一个坐标：你站在这里，才会知道自己身处何时何地，究竟在追什么，又究竟遗忘了什么、错失了什么。  
> 因此我们探究尽头：不是为了更漂亮的叙事，而是为了在选择之前先看清代价，在行动之后仍能回到现实，把喜悦与疼痛都纳入复盘，逼近那个“其实可以更好”的自己。
>
> “拥有了一双能看透迷雾，直抵本质的眼睛。”

> 目标：把“做更好的选择”变成一套**可证伪 / 可退出 / 可复盘**、可长期迭代的系统。  
> 核心信念：**选择质量（方向与乘数）长期大于努力强度（执行与燃料）**。

---

## 核心：知识管理 3.0（AI 知识工厂）

这份手册把“知识管理”当作一件工程问题：不是收集笔记，而是让洞见可持续地产出、可验证、可复盘。

- **1.0 给你柜子（文件夹）**：能收纳，但世界是网状的；排他分类会让检索与组合越来越难。  
- **2.0 给你地图（双链图谱）**：能连接，但当节点到数千/上万时，连接的潜在组合爆炸，人脑带宽无法遍历；图谱会从星图变成乱麻。  
- **3.0 给你生产线（可显式化设计并自动运行的工作流）**：把“高强度、可重复的认知劳动”流水线化：
  - **自动清洗**：长文/材料 → 核心论点/结构/变量  
  - **自动关联**：从全库压缩出可审的候选集（10–30 条）  
  - **自动重述（最关键）**：抽旧卡片 → 在新语境下重写/合并/找冲突 → 把“存了就忘”变成持续显化  
  - **审计/回滚**：关键结论必须能回链到证据锚点，否则就降级为观察名单

在 3.0 里，人类不是操作工，而是**知识工厂指挥官**，只做三件事：

1) **提出好问题**（方向盘）  
2) **提供高质量上下文**（结构化养料：锚点/变量/约束/时间窗）  
3) **做价值判断并签字**（哪种组合更有洞见、符合价值观、值得承担代价与责任）

> 本项目把这套“生产线”落在 4 层资产结构里：`sources`（材料可回查）→ `world_understanding`（机制与预测）→ `meta`（可证伪猜想与证据升级）→ `distilled`（可复用结论与门禁）。

这条生产线有两档“引擎”（也是你最常用的两套框架）：

- **Framework 05（推理工具箱）= 生产线工序卡**：材料→结构→推演→行动（默认先用，短而密，可套用任何主题）。  
- **Framework 06（时空穿越×终局推演）= 重武器**：当你要回答“是不是 BTC 级（10x/100x/1000x）/要 Gate 1/2/3 强结论/要终局地图”时才启用（强制标题、强制证伪、强制停机点）。

## Cursor Quickstart（只看这一段就够 / 复制粘贴就能用）

### 0) 默认入口（你贴任何东西都行）→ `/inbox`

在 Cursor Chat 输入：`/inbox`，把文章/事件/线索贴进去即可。  
它会自动路由到 `/article-digest`（默认，Framework 05）/ `/event-reasoning` / `/time-travel-06` 并落盘。

### 1) 真实事件推理（投资/政策/监管/公司资本动作）→ `/event-reasoning`

在 Cursor Chat 输入：`/event-reasoning`，把事件描述 + 链接贴进去即可。  
你会得到 3 个落盘文件（证据表 / IC memo / mini-06），并且每个情景都带 `observables`（可观测指标）。

### 2) 新文章/材料变资产（sources → world_understanding）→ `/article-digest`

在 Cursor Chat 输入：`/article-digest`，把文章全文（或要点）+ 链接贴进去即可。  
你会得到：`sources` digest + `world_understanding` 主文 + 两个索引更新。

### 3) “BTC 式百倍/千倍”极限推演（强结论门禁）→ `/time-travel-06`

在 Cursor Chat 输入：`/time-travel-06`，把候选/材料 + 链接贴进去即可。  
你会得到：按 06 固定标题输出的终局推演（Gate/Tripwire/Bound/最短探针），并按需落盘到 `world_understanding/`。

---

## 工作流路由器（你不用解释你要我做什么）

- **你想省事（默认入口）** → 用 `/inbox`（自动路由）  
- **你给的是“文章/观点/材料”** → 用 `/article-digest`（把材料变资产）  
- **你给的是“正在演进的真实事件”（监管/政策/资本配置/供需/技术拐点）** → 用 `/event-reasoning`（把不确定未来变成情景树+停机点）  
- **你要 BTC 式强结论/穿越推演/终局地图** → 用 `/time-travel-06`（Framework 06：把强结论写成可证伪门禁）

> 命令文件位置：`.cursor/commands/`（你可以在 Cursor Chat 里直接调用）

---

## 按目标阅读（更省脑）

- **你正在做一个现实选择（职业/关系/项目/学习）**：从 `worksheets/decision_one_pager.md` 开始，用一页卡落地  
- **你想训练“尽头 + 退出条件”的能力**：读 `frameworks/03_end_thinking_tangnuo.md`  
- **你要把“观点”升级成“系统”**：读 `distilled/life_choice_operating_system.md`  
- **你给我新文章/线索，想把它变成可用结论**：看下面的“文章处理工作流”
- **你要用 Case Atlas 做类比门禁**：先看 `world_understanding/yearbook/README.md` 的“统一应用方法”，按 **速用索引 → Tripwire/Bound/Spiral → 最短探针** 落地

---

## 建议阅读路线（Suggested Reading Path，传统线性版）

### 入门（先能用）
1. `principles/01_choice_over_effort.md`：先把“选择 vs 努力”的边界说清楚  
2. `worksheets/decision_one_pager.md`：直接用一页卡做一次真实决策  
3. `frameworks/03_end_thinking_tangnuo.md`：加入“尽头坐标”，写出退出条件

### 进阶（把决策质量做高）
1. `frameworks/01_decision_quality.md`：用“过程质量”替代“结果执念”  
2. `frameworks/04_horizon_map.md`：短/中/长期利益的统一视角  
3. `frameworks/02_opportunity_and_option_value.md`：机会成本与期权价值（保留选择）
4. `frameworks/05_reasoning_toolkit.md`：推理工具箱（材料→结构→推演→行动）

### 熟练（用案例训练直觉）
- 进入 `cases/`：每个案例都带“尽头 + 退出条件 + 下一步实验”

---

## 核心入口

| 模块 | 链接 | 说明 |
|---|---|---|
| **原则** | `principles/README.md` | 选择观、价值与边界 |
| **框架库** | `frameworks/README.md` | 可复用的决策模型与方法 |
| **世界理解** | `world_understanding/README.md` | 对世界/技术/机制的解释模型（趋势/范式/路线） |
| **练习表单** | `worksheets/README.md` | 可复制填写：one-pager / premortem / postmortem |
| **案例库** | `cases/README.md` | 跨场景训练：职业/关系/健康/金钱/项目 |
| **清单** | `checklists/README.md` | 高频场景：跳槽/合作/学习路径/项目选择等 |
| **材料库** | `sources/README.md` | 外部材料 digest（可回查，避免编造） |
| **证据联结** | `meta/README.md` | 猜想注册表 + 决策日志：新证据验证旧猜想，升级确定性 |
| **蒸馏层** | `distilled/README.md` | 给人看的精华入口：核心猜想 + 高确定性决策 |
| **年度复盘** | `distilled/yearbook/README.md` | 2000–2025 年度参照系：短版入口（长版在 `world_understanding/yearbook/`） |

---

## 关于“尽头”（引用）

> “极限的思索让我们箭一样射向远方，但注视它实际上的力竭停止之处，转而追究它‘本来可以发生却为什么没发生’、‘已堪堪发生却退回去复归不会发生’，则让我们老老实实落回此时此地来，这比较迫切，也有更多不舒服的真相，尤其是人自身的真相。  
>  
> 事物在此一实然世界的确实停止之处，我称之为尽头。在这里，一次一次的，最终，总的来说，揭示的是人的种种真实处境。”——唐诺

## 文章处理工作流（Article Processing Workflow）

当你给我一篇文章时，我会把它变成“四层资产”（你在 GitHub 上一眼能找到）。  
你可以把它理解成一条**知识生产线**：材料进入 → 清洗 → 关联 → 重述/合并 → 证据升级 → 结论沉淀。

- **sources/**：可回查 digest（锚点/定义/变量/机制/预测/不确定性）  
- **world_understanding/**：机制推演与门禁落地（默认按 Framework 05；需要终局/Gate 强结论时升级到 Framework 06）  
- **meta/**：猜想注册表/决策日志（让新证据能验证旧猜想并升级确定性）  
- **distilled/**：给人看的结论（结论+证据锚点+反证信号+下一步）

```mermaid
flowchart TD
  ArticleInput[ArticleInput] --> MaterialClassify[MaterialClassify]
  MaterialClassify --> RecallExisting[RecallExisting]
  RecallExisting --> ExtractAssets[ExtractAssets]
  ExtractAssets --> DraftExploration[DraftExploration]
  DraftExploration --> Converge[Converge]
  Converge --> DecideLanding{DecideLanding}

  DecideLanding --> LandFrameworks[LandFrameworks]
  DecideLanding --> LandPrinciples[LandPrinciples]
  DecideLanding --> LandCases[LandCases]
  DecideLanding --> LandChecklists[LandChecklists]
  DecideLanding --> LandWorksheets[LandWorksheets]

  LandFrameworks --> WriteSourcesDigest[WriteSourcesDigest]
  LandPrinciples --> WriteSourcesDigest
  LandCases --> WriteSourcesDigest
  LandChecklists --> WriteSourcesDigest
  LandWorksheets --> WriteSourcesDigest

  WriteSourcesDigest --> UpdateSourcesIndex[UpdateSourcesIndex]
  UpdateSourcesIndex --> UpdateModuleIndex[UpdateModuleIndex]
  UpdateModuleIndex --> NextReading[NextReading]
```

### 你会得到什么（默认交付）

- **1 个 digest**：`sources/YYYY-MM-DD_xxx.md`
- **1 个 world_understanding 主文**：`world_understanding/xxx.md`  
  - 默认按 `frameworks/05_reasoning_toolkit.md` 的骨架做“短而密”的推理与落地  
  - 若用户点名 06 / 要 BTC 式强结论 / 新 repo 分析 → 跑 `/time-travel-06`，按 `frameworks/06_time_travel_endgame_simulator.md` 固定标题完整输出（标题不可省），并落盘到 `world_understanding/<slug>_endgame_06.md`
- **1 段“重述/合并”（知识工厂工序）**：  
  - 从旧库抽取 2–3 个相关节点（或相互矛盾的节点），写出一段“合并后的新表述”，并标注 1 个冲突点与后续探针  
- **1 条可证伪猜想（或更新旧猜想）**：写入 `meta/hypotheses_registry.md`
- **1 条蒸馏结论入口**：更新 `distilled/opportunity_map.md`（必要时也更新 `distilled/core_hypotheses.md`）
- **联结检查（小门禁）**：至少命中 1 条旧 `H-XXXX`（支持/反对/不确定三选一），并把交叉链接回写到 `meta/hypotheses_registry.md`（让新证据能升级旧猜想）

---

## 真实事件推理工作流（Event Reasoning Workflow，适合投资/政策/监管）

当你不是在“消化一篇文章”，而是在处理一个**正在演进的真实事件**（例如：制裁/出口管制/监管调查/产业政策/市场结构变化），推荐直接用事件推理工具把它落成可执行 memo：

- **入口**：`tools/event_reasoning/README.md`
- **你在 Cursor 里最短发起方式**：  
  直接对大模型说：请按 `tools/event_reasoning` 的规范把下面事件跑一遍，并输出 memo/mini06/证据表（我给你链接/线索…）

**你会得到什么（默认交付）**
- `sources/YYYY-MM-DD_event_reasoning_<event_id>.md`：证据表（可审计，含反证与盲点）
- `world_understanding/event_reasoning_runs/YYYY-MM-DD_<event_id>_memo.md`：1 页 IC memo（结论/机制/情景/行动/停机点）
- `world_understanding/event_reasoning_runs/YYYY-MM-DD_<event_id>_mini06.md`：门禁版（Tripwire/Bound/Spiral/最短探针）

**为什么它和“文章工作流”不同**
- 文章工作流更像“把材料变资产”；事件推理工作流更像“把不确定未来变成可下注的情景树 + 停机点”。

## 写作视角说明（Future Historian / 未来回看者）

这个手册默认用一种“更有趣但更负责”的写法：

- **像未来研究员在写**：允许更强的镜头感与叙事，但关键推演必须落回：**事实/假设/推演标签** + **可回归信号** + **下一步行动**。
- **像站在当时的人身上回看历史**：写清“当时的年代背景、当时能看到什么/看不到什么、当时有哪些可选路径与代价”，并显式区分“当时信息”与“事后上帝视角”。
- **追求更确定的未来**：不靠玄学，靠“机制不变量 + 约束 + 信号”，用 20%/50%/80% 的确定性阶梯持续更新。

## 一句话总流程（你每次做选择都能照做）

```mermaid
flowchart TD
  start[Start] --> frame[FrameProblem]
  frame --> options[GenerateOptions]
  options --> reversible{Reversible?}
  reversible -->|Yes| buyOption[BuyOptionSmallBet]
  reversible -->|No| endCheck[EndThinkingCheck]
  buyOption --> endCheck
  endCheck --> horizon[HorizonMapShortMidLong]
  horizon --> decide[DecideAndSetExitCriteria]
  decide --> act[Execute]
  act --> review[ReviewPostmortem]
  review --> start
```

---

## 项目结构

```
choice-handbook/
├── README.md
├── AGENT.md
├── sources/
├── principles/
├── frameworks/
├── world_understanding/
├── worksheets/
├── cases/
└── checklists/
```

---

## 使用建议（避免变成鸡汤）

- **每一篇都必须落到行动**：至少一个下一步实验（小成本验证/访问/试运行）；Plan Prompt 仅在需要更长执行指令时才写（否则链接到 `AGENT.md` 模板）。
- **每一个选择都必须写“退出条件”**：何时停止、止损、停机点，以及重启条件。
- **用“尽头”把你拉回现实**：看清资源、约束、代价与人自身的真实处境。
- **让新证据升级确定性**：当新高可信材料验证/反证旧猜想时，要更新 `meta/hypotheses_registry.md` 与 `meta/decisions_log.md` 并回写双向链接。

