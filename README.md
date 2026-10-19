# ROS 2 Four-DOF Robotic Arm

URDF model of a four-degree-of-freedom arm with RViz visualization, joint sliders, and TF inspection. Created by Haresh Selvakumar.

## Contents

- `src/four_dof_arm_description/`: ROS 2 description package, launch file, and RViz configuration.
- `evidence/`: submitted screenshots and TF tree.
- `ROS2_4DOF_Arm_Haresh_Report.pdf`: project report, with an editable DOCX alongside it.

## Build and launch

Use a Linux ROS 2 installation with `colcon`, `robot_state_publisher`, `joint_state_publisher_gui`, and `rviz2`. Source your installed ROS 2 distribution before running these commands from this repository:

```bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
ros2 launch four_dof_arm_description display.launch.py
```

Move the joint sliders to inspect arm poses. The provided launch file starts the state publisher, joint GUI, and RViz together.

## Scope and validation

This package describes and visualizes the arm; it does not implement motor control, motion planning, or a physics simulation. The supplied screenshots document prior execution. The current packaging check parses XML and Python source; a ROS 2 build and interactive RViz session have not been rerun here.
