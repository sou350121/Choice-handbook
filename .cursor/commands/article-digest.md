# /article-digest — Choice Handbook 文章→资产（sources → world_understanding）

面向：使用 Cursor 交互的大模型用户。  
目标：把你贴的文章/材料变成 **可回查 digest + 可复用世界理解**，并更新索引。

## 你对模型怎么说（复制粘贴）

请按 `choice-handbook` 的“文章处理工作流”处理下面材料，并把产物落盘：

1) 生成一个 `sources` digest（保留原文 + 可核验锚点 + 可抽取资产 + 不确定性），落盘到：  
   `choice-handbook/sources/YYYY-MM-DD_<slug>_paste.md`
2) 生成一个 `world_understanding` 主文（机制/变量/预测/探针/退出重启），落盘到：  
   `choice-handbook/world_understanding/<slug>.md`  
   - 要求：用“短而密”的结构写，必须包含：机制链（箭头）/ 变量表（≤10）/ 3 情景（概率+时间窗+observables）/ 48h-7d-30d 探针 / 退出条件+重启条件
   - 知识工厂工序（强制）：补一段“重述/合并”——从旧库抽取 2–3 个相关节点（或矛盾节点），写出合并后的新表述，并标注 1 个冲突点 + 1 个最小探针
3) 更新索引：  
   - `choice-handbook/sources/README.md`  
   - `choice-handbook/world_understanding/README.md`
4) 如果材料足够“可证伪”，补 1 条（或更新旧）猜想到：`choice-handbook/meta/hypotheses_registry.md`（不确定就跳过，不要硬写）

这是材料全文与链接（若无链接也可以）：
<粘贴全文 / 要点 / 链接列表>

## 默认产出（你会看到的文件）

- `choice-handbook/sources/YYYY-MM-DD_<slug>_paste.md`
- `choice-handbook/world_understanding/<slug>.md`
- 两个 README 索引更新（sources / world_understanding）

