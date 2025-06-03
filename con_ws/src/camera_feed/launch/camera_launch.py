from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    image_topic_arg = DeclareLaunchArgument(
        'image_topic',
        default_value='/camera/image_raw',
        description='Topic to subscribe to for camera feed'
    )
    return LaunchDescription([
        Node(
            package='camera_feed',
            executable='image_node',
            name='camera_publisher'
        ),
        image_topic_arg,
        Node(
            package='camera_feed',
            executable='show_feed',
            name='camera_subscriber',
            parameters=[{'image_topic': LaunchConfiguration('image_topic')}]
        ),
    ])