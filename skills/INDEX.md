# Skills 索引（给 Cursor 用的）

用法：在对话里输入 `@skills/文件名.md`，再告诉我“按这个 skill 做”。

最短用法：
- 不写任何东西：我会自动决定要不要启用 skill。
- 强制启用：你先写 `@skills/xxx.md` 再说需求。
- 禁用：你说“这次不要用 skills”。

## 推荐从这里开始（最常用）
- `@skills/skill_code_change.md`：写代码/改代码/重构（最常用）
- `@skills/skill_sqlite.md`：本地 SQLite 建库、查表、写查询
- `@skills/skill_testing.md`：写测试、补测试、提高覆盖
- `@skills/skill_web_automation.md`：Playwright 自动化网页/E2E/复现前端问题
- `@skills/skill_docs_digest.md`：读内部文档、整理规范、输出可执行结论
- `@skills/skill_x_longform_upwriter.md`：写技术 Up 主长文（X 单条长帖 + 预告 + Telegram 长文）

## 工程必备（建议你记住）
- `@skills/skill_debug.md`：系统化 Debug（复现→定位→修复→回归）
- `@skills/skill_code_review.md`：代码评审清单（正确性/安全/性能/测试）
- `@skills/skill_security.md`：安全与隐私加固（最小权限/校验/脱敏）
- `@skills/skill_performance.md`：性能优化（先量化再优化）
- `@skills/skill_architecture.md`：需求拆解与方案设计（对比/风险/迁移）
- `@skills/skill_setup_dependencies.md`：环境与依赖搭建（少污染系统、可复现）
- `@skills/skill_data_analysis.md`：数据清洗/分析/导入导出（CSV/Parquet/SQLite）
- `@skills/skill_release_changelog.md`：发版/变更日志/升级与回滚

## Cursor Rules 专用（让自动化更稳）
- `@skills/skill_cursor_rules_authoring.md`：编写/拆分 `.cursor/rules/*.mdc`（alwaysApply/globs/避免冲突）
- `@skills/skill_cursor_rules_router.md`：维护 `skills-router.mdc`（关键词路由、禁用/强制约定）
- `@skills/skill_cursor_rules_debug.md`：排查 rules 不生效/乱生效（位置/格式/冲突/触发范围）

## Cursor 专用（强烈推荐）
- `@skills/skill_cursor_repo_onboarding.md`：快速上手项目（找入口/怎么跑/怎么测）
- `@skills/skill_cursor_mcp_setup.md`：配置 MCP（mcp.json）与安全白名单

## 小白安全规则（强烈建议遵守）
- 只允许操作项目目录（例如 `D:\\Project_dev`），不要开放整盘。
- 数据库优先用 dev/test；生产库仅只读并最小权限。
- 密码/token 不写死在文件里，优先用环境变量。

