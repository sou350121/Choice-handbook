# /traveler-judge — 穿越者投资判官（Framework 07）

面向：使用 Cursor 交互的大模型用户。  
目标：把“最大必然性 × 低估”写成**可验证推理**（区间+敏感度），并输出一份**自然语言**的判官报告（严格 1–7 结构）。

## 你对模型怎么说（复制粘贴）

请按 `choice-handbook/frameworks/07_future_traveler_investing_judge.md` 的规则与固定输出结构执行，并严格遵守：

- **as-of 日期卫生**：不得使用任何晚于 as-of 日期的信息；不确定是否晚于 → 视为不可用。
- **严禁装作确定**：数据不全就写“区间 + 敏感度”。
- **必须算量级**：供需与边际效益要“算”出量级，并给 Base/Bull/Bear。
- **最多追问 1 个关键参数**：其余缺口用假设+敏感度处理。
- **语气自然**：不要工程化，但 1–7 标题必须保留。

输出完成后，把产物落盘：

- `choice-handbook/world_understanding/traveler_judge_runs/YYYY-MM-DD_<scope>_judge.md`
- 并在 `choice-handbook/world_understanding/traveler_judge_runs/README.md` 里追加一行索引（文件名 + 1 句最大必然性）

如果你在输出中引用了任何外部链接或具体数据点（非用户提供），请额外落盘：

- `choice-handbook/sources/YYYY-MM-DD_traveler_judge_<scope>_evidence.md`
- 并把它加进 `choice-handbook/sources/README.md`

这是输入（可以直接粘贴你的提示词或任何材料）：
<PASTE_HERE>
