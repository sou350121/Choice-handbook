# Build & Run（ROS 2）

> 本文是“能跑起来”的最小 runbook。具体 driver/launch 细节会随着硬件接口落地而补齐。

## 1) 前置
- 已安装 ROS 2（发行版与 OS 版本请在此补充：TODO）
- 已安装 `colcon` 与常用工具链

## 2) 构建

```bash
cd Violin_Robot_PRD/ws
colcon build --symlink-install
```

构建后：

```bash
source install/setup.bash
```

## 3) 启动（占位）
启动入口建议统一由 `violin_robot_bringup` 提供。
```bash
# v0：启动最薄垂直切片（mock driver + music + policy stub + tactile guard）
cd Violin_Robot_PRD/ws
source install/setup.bash
ros2 launch violin_robot_bringup v0_mock.launch.py
```

## 4) 常见问题
- **找不到 package**：确认已 `source install/setup.bash`
- **参数散落**：所有运行参数必须放入 `configs/`，不要硬编码
