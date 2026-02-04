# latex-uiux

为 **Knownote LaTeX Writer**（三栏布局 + Codex bottom sheet + PDF 预览）做“像产品”的 UI/UX 美化与可用性提升。

本命令会使用本仓库内置的 **UI UX Pro Max** 数据库：`.shared/ui-ux-pro-max/`，通过搜索得到风格/配色/字体/UX guideline，然后把它落实为可 review 的代码改动。

## 适用场景

- “界面不够美 / 不够像 Overleaf / 不够像 Cursor”
- “信息层级混乱、边框太多、留白不一致、字体不统一”
- “Diff/Apply 不够显眼、控制按钮滚动后找不到”
- “需要一套统一的视觉规范（颜色、字体、间距、状态）并落地到组件”

## 工作流（请严格按顺序）

### 1) 定义目标与约束（1 分钟）

输出这些要点（越短越好）：
- **目标用户**：Overleaf/LaTeX 用户（偏专业/效率）
- **关键任务**：写作、编译、看预览、审 diff、应用/撤销
- **硬约束**：不改业务逻辑优先；不破坏现有快捷键/拖拽；Electron + React + Tailwind/shadcn

### 2) 用 UI UX Pro Max 搜索（必须跑 5 次以上）

> Windows 直接用 `python`；其它系统用 `python3` 亦可。

```powershell
# Product: editor / IDE / writing tool
python .shared\ui-ux-pro-max\scripts\search.py "editor ide writing tool" --domain product -n 5

# Style: choose 1–2候选（偏专业、低噪声）
python .shared\ui-ux-pro-max\scripts\search.py "minimal dark saas professional" --domain style -n 8

# Typography: 字体组合 + 层级
python .shared\ui-ux-pro-max\scripts\search.py "professional modern ui" --domain typography -n 6

# Color: SaaS / productivity
python .shared\ui-ux-pro-max\scripts\search.py "saas productivity dark" --domain color -n 6

# UX: IDE / editor 常见可用性规则
python .shared\ui-ux-pro-max\scripts\search.py "editor ide panel layout" --domain ux -n 12

# Stack: React（本项目 renderer）
python .shared\ui-ux-pro-max\scripts\search.py "shadcn tailwind" --stack react -n 10
```

### 3) 输出一页 UI Spec（先定标准，再改代码）

必须包含：
- **风格选择**（只选 1 个主风格 + 1 个备用）
- **颜色规范**：background/surface/border/text/primary/success/error（给出 token 名称与用途）
- **字体与层级**：title/section/label/body/mono（字号/字重/行高）
- **组件规范**：卡片/分割线/按钮/标签/空状态（减少“套娃边框”）
- **交互规范**：sticky 工具条、可拖拽句柄、loading/成功/失败反馈

### 4) 落地到代码（小步提交、可回退）

优先修改这些文件（按实际项目存在情况调整）：
- `ai-latex-editor/desktop/knownote/src/renderer/src/components/pages/LatexWriterPage.tsx`
- `ai-latex-editor/desktop/knownote/src/renderer/src/assets/main.css`
- 相关 UI 组件（shadcn）与布局组件（ResizableLayout 等）

改动原则：
- **减少边框层级**：边框只用于分组边界；容器层尽量用背景层级区分
- **统一半径/阴影**：1 套 radius（例如 8/12）+ 2 档 shadow（sm/lg）
- **统一间距**：以 4/8/12/16 为基准，避免 3/5/7
- **把关键操作放到视线中心**：Diff/Apply/Undo/Compile 状态优先

### 5) 自测清单（必须做）

- 拖拽分割线在 PDF iframe 上方也能顺滑
- Codex 工具条 sticky，滚动后仍可 Apply/Undo
- 深色/浅色模式对比度可读（尤其 diff + 错误红/成功绿）
- 空状态清晰，不会“看起来像坏了”

