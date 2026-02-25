# AGENTS.md

## Cursor Cloud specific instructions

This is a **pure Markdown knowledge base** (选择手册 / Choice Handbook) — there is no executable code, no package manager, no build system, and no application server.

### Repository overview

- **133 Markdown files** organized into 10 topic directories (see `README.md` "核心入口" table for the full map).
- Writing and content conventions are defined in `AGENT.md` and `agent_constitution.md` — follow those when creating or editing content.
- `.gitattributes` enforces LF line endings for `.md` files.

### Lint

```bash
markdownlint-cli2 "**/*.md"
```

`markdownlint-cli2` is installed globally via npm. The repo does not ship a `.markdownlint.jsonc` config, so default rules apply. Expect ~1200 style warnings (mostly `MD013` line-length / `MD022` blanks-around-headings / `MD032` blanks-around-lists) — these are informational, not blocking.

### Cross-reference validation

Internal links between documents (439 total) can be validated with a simple Node.js one-liner — all real references resolve; the only "broken" entries are intentional placeholders (`xxx.md`, `YYYY.md`, `snake_case.md`).

### No services to run

There is no backend, frontend, database, or Docker dependency. The "development environment" is Git + a text editor + `markdownlint-cli2` for optional linting.

### Content workflow

When adding or modifying articles, follow the "四层资产" (four-layer asset) workflow described in `AGENT.md` and the "证据联结" (evidence linking) protocol. Always update the relevant directory `README.md` index when adding/renaming files.
