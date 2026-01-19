# 06 降维解剖：把一个学科/领域压到“可计算的骨架”

当用户输入一个学科或领域（例如“推荐算法”“LLM”“宏观经济学”“免疫学”“量化交易”），你要做的不是堆概念，而是把它“压缩”成：
- 它在解决什么根本矛盾？
- 它的变量是什么？
- 它的互动算子（定律/机制）是什么？
- 它如何被形式化（数学/伪代码）？

这会把讨论从修辞与类比，拉回到可检验与可复用。

---

## 步骤 1：第一性原理扫描（First Principles Scan）

目标：剔除类比、修辞、次级知识，只保留物理层或逻辑层真理。

输出格式（建议）：
- 事实（可验证）：
- 约束（不可违背）：
- 资源（可用的）：
- 风险（不可忽视的）：

---

## 步骤 2：提取根本问题 \(\\mathcal{O}\\)（Objective）

目标：识别核心矛盾，定义目标函数。

输出格式（建议）：
- \(\\mathcal{O}(\\cdot)\\) 要最大化/最小化什么？
- 决策变量是什么？
- 约束条件是什么？
- 评价指标与损失的冲突在哪里？

例（抽象模板）：
\[
\\max_{a\\in\\mathcal{A}} \\; \\mathbb{E}[R(a)] \\quad \\text{s.t.}\\quad C(a)\\le \\text{Budget},\\; \\text{Risk}(a)\\le \\tau
\]

---

## 步骤 3：构建根本骨架（Variables & Operators）

### 3.1 核心变量（原子单元）
把领域拆成最小变量集合（不超过 10 个，越少越好）：
- 状态 \(S\)
- 行为/决策 \(A\)
- 观测 \(X\)
- 参数 \(\\theta\)
- 数据 \(D\)
- 约束/预算 \(B\)
- 风险 \(\\mathcal{R}\\)
- 反馈/回报 \(R\)

（具体领域可以替换：例如推荐里是 user/item/context；经济里是价格/供给/需求/预期；生物里是浓度/速率/能量等）

### 3.2 核心定律（互动算子）
写出“变量如何相互作用”的算子（不超过 5 条）：
- 转移：\(S_{t+1}=f(S_t, A_t, \\epsilon)\\)
- 观测：\(X_t=g(S_t, \\eta)\\)
- 目标：\(R_t=h(S_t, A_t)\\)
- 学习/更新：\(\\theta \\leftarrow \\text{Update}(\\theta, D)\\)
- 约束：\\(\\text{Risk}(\\cdot),\\;\\text{Cost}(\\cdot)\\)

---

## 步骤 4：形式化映射（Math / Logic Pseudocode）

目标：把以上内容转成“可执行的逻辑”，便于推演与验证。

伪代码模板：

```text
Given: Data D, constraints B, risk limit τ
Define: variables V = {S, A, X, θ, ...}
Define: operators {f, g, h, Update}

Objective: maximize O(θ) subject to constraints

loop:
  observe X
  infer state S = infer(X, θ)
  choose action A = policy(S, θ)  // decision
  get feedback R = h(S, A)
  update θ = Update(θ, (X, A, R))
  if exit_condition_met(): break
```

---

## 交付要求：必须有“当下与未来”的可观测信号

降维解剖不是为了抽象而抽象。最后必须落回：
- 当下：哪些变量正在主导系统？
- 未来：哪些变量一旦变化，系统会切换到另一阶段？
- 信号：用什么可观测指标判断阶段切换？

---

## 练习：任选一个领域，写出 1 页骨架

用下面标题快速填空（控制在一页）：
1. 第一性原理扫描（事实/约束/资源/风险）
2. 根本问题 \(\\mathcal{O}\\)（目标函数 + 决策变量 + 约束）
3. 变量表（≤10）
4. 互动算子（≤5）
5. 伪代码（≤30 行）
6. 阶段切换信号（3 个）

