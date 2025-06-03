from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='teleop',
            executable='teleop',
            name='teleop_twist_stamped'
        ),
    ])