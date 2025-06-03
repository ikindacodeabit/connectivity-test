import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
import sys
import tty
import termios
import time


def get_key():
    """Read single keypress from stdin."""
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


class TeleopTwistNode(Node):
    def __init__(self, use_stamped: bool):
        super().__init__('teleop_twist_node')
        self.use_stamped = use_stamped

        if self.use_stamped:
            self.publisher = self.create_publisher(TwistStamped, 'cmd_vel_stamped', 10)
        else:
            self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.current_twist = Twist()

    def timer_callback(self):
        if self.use_stamped:
            msg = TwistStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.twist = self.current_twist
            self.publisher.publish(msg)
        else:
            self.publisher.publish(self.current_twist)

    def update_twist_from_key(self, key):
        linear = 0.5
        angular = 0.5

        if key == 'w':
            self.current_twist.linear.x = linear
            self.current_twist.angular.z = 0.0
        elif key == 's':
            self.current_twist.linear.x = -linear
            self.current_twist.angular.z = 0.0
        elif key == 'a':
            self.current_twist.linear.x = 0.0
            self.current_twist.angular.z = angular
        elif key == 'd':
            self.current_twist.linear.x = 0.0
            self.current_twist.angular.z = -angular
        elif key == ' ':
            self.current_twist = Twist()
        elif key == 'q':
            rclpy.shutdown()


def main(args=None):
    global settings
    settings = termios.tcgetattr(sys.stdin)

    print("Select message type to publish:")
    print("1. geometry_msgs/msg/Twist")
    print("2. geometry_msgs/msg/TwistStamped")
    choice = input("Enter 1 or 2: ").strip()

    use_stamped = choice == '2'

    rclpy.init(args=args)
    node = TeleopTwistNode(use_stamped)

    try:
        print("Use keys: W/A/S/D to move, SPACE to stop, Q to quit.")
        while rclpy.ok():
            key = get_key()
            node.update_twist_from_key(key)
            rclpy.spin_once(node, timeout_sec=0.1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
