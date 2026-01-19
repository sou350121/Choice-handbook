# Choice Handbook（选择手册）

> 目标：把“做更好的选择”变成一套可练习、可复盘、可长期迭代的系统。
>
> 核心信念：**选择质量（方向与乘数）长期大于努力强度（执行与燃料）**。

---

## 建议阅读路线（Suggested Reading Path）

### 入门（先能用）
1. `principles/01_choice_over_effort.md`：先把“选择 vs 努力”的边界说清楚  
2. `worksheets/decision_one_pager.md`：直接用一页卡做一次真实决策  
3. `frameworks/04_end_thinking_tangnuo.md`：加入“尽头坐标”，写出退出条件

### 进阶（把决策质量做高）
1. `frameworks/01_decision_quality.md`：用“过程质量”替代“结果执念”  
2. `frameworks/02_horizon_map.md`：短/中/长期利益的统一视角  
3. `frameworks/03_opportunity_and_option_value.md`：机会成本与期权价值（保留选择）
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

---

## 关于“尽头”（引用）

> “极限的思索让我们箭一样射向远方，但注视它实际上的力竭停止之处，转而追究它‘本来可以发生却为什么没发生’、‘已堪堪发生却退回去复归不会发生’，则让我们老老实实落回此时此地来，这比较迫切，也有更多不舒服的真相，尤其是人自身的真相。  
>  
> 事物在此一实然世界的确实停止之处，我称之为尽头。在这里，一次一次的，最终，总的来说，揭示的是人的种种真实处境。”——唐诺

## 文章处理工作流（Article Processing Workflow）

当你给我一篇文章时，我会把它“读入 → 回看旧内容 → 提炼 → 落盘 → 复盘”，并把产出放到最合适的位置（`frameworks/`/`cases/`/`checklists/`/`worksheets/`/`principles/`），同时沉淀一份 `sources/` digest 以便后续回查。

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

- **每一篇都必须落到行动**：至少一个下一步实验（小成本验证/访问/试运行）+ **一个可复制执行的 Plan Prompt**（直接贴给 Agent 去完成）。
- **每一个选择都必须写“退出条件”**：何时停止、止损、停机点，以及重启条件。
- **用“尽头”把你拉回现实**：看清资源、约束、代价与人自身的真实处境。

