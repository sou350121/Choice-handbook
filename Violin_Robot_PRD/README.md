# Violin Robot（天工 × 零巧手）工程 SSOT

本目录是本项目的**开发主工程**（ROS 2）与**单一真实来源（SSOT）**所在地：PRD/设计/接口契约/配置/校准/工具/运行手册都以此为准。

## 快速入口

- **PRD（验收口径）**：`PRD.md`
- **DESIGN（系统设计）**：`DESIGN.md`
- **技术路线与决策原则**：`AGENT_robotExpert.md`
- **PRD 对齐计划**：`PRD_PLAN.md`

## 工程目录（你应该从这里开始）

- **ROS 2 Workspace**：`ws/`
  - `ws/src/`：ROS 2 packages（包边界就是物理导轨）

- **SSOT：契约层**：`contracts/`
  - `contracts/ros_interfaces/`：topic/service/action 规范（人类可读）
  - `contracts/frames/`：坐标系与 tf 树规范（人类可读）
  - `contracts/data_schema/`：数据/episode schema 与时间同步规范
  - `contracts/safety/`：限位/速度/力矩/急停策略（默认约束）

- **SSOT：配置层**：`configs/`
  - `configs/hardware/`：硬件与序列号绑定配置（driver 参数）
  - `configs/control/`：控制器与限幅配置
  - `configs/demo/`：demo profile（场地/琴/弓/曲目）配置

- **SSOT：校准层**：`calibration/`
- **工程文档（runbooks）**：`docs/engineering/`
- **工具与脚本**：`tools/`
- **数据注册表（pointers-only）**：`data_registry/`（只存外部位置/版本/统计，不存大文件）

## SSOT 规则（最小但强约束）

- **物理导轨**：新增功能必须放进正确的 ROS2 package；禁止“到处扔脚本”。
  - packages 的依赖关系以 `contracts/ros_interfaces/` 与包职责为准。
- **契约优先（contract-first）**：先改 `contracts/` 再改实现；实现必须对齐契约。
- **pointers-only**：视频/音频/触觉原始流/模型权重不入库，只登记在 `data_registry/`。

## GitHub 联动（索引层）

- Issue/PR 只做索引与协作，不承载正文；正文以本目录内 canonical 文档为准。
- Issue 必须链接到本目录内的 canonical 文档（PRD/设计/契约/决策/复盘）。
