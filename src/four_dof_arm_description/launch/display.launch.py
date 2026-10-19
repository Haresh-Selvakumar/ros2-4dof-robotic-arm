from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Find this package's installed files.
    package_dir = Path(
        get_package_share_directory("four_dof_arm_description")
    )

    # Read the robot model as text.
    urdf_file = package_dir / "urdf" / "four_dof_arm.urdf"
    robot_description = urdf_file.read_text()

    # Calculate and publish the link transforms.
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}],
        output="screen",
    )

    # Provide sliders for the four movable joints.
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        parameters=[{"robot_description": robot_description}],
        output="screen",
    )

    # Open the robot visualization application.
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", str(package_dir / "rviz" / "arm.rviz")],
        output="screen",
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz,
    ])
