#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
import sys
import termios
import tty
import select
from datetime import datetime

# Key mappings
move_bindings = {
    'w': (1.0, 0.0, 0.0),
    's': (-1.0, 0.0, 0.0),
    'a': (0.0, 1.0, 0.0),
    'd': (0.0, -1.0, 0.0),
    'q': (0.0, 0.0, 1.0),
    'e': (0.0, 0.0, -1.0)
}

speed_bindings = {
    't': 1.1,
    'g': 0.9
}

def get_key():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    key = sys.stdin.read(1) if rlist else ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


class TeleopTwistStamped(Node):
    def __init__(self):
        super().__init__('teleop_twist_stamped')
        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel_stamped', 10)
        self.linear_speed = 0.5
        self.angular_speed = 1.0
        self.timer = self.create_timer(0.1, self.publish_zero_twist)
        self.last_key_time = self.get_clock().now()

        self.get_logger().info("Use keys: w/s/a/d/q/e to move. t/g to adjust speed. Ctrl+C to exit.")

    def publish_twist(self, linear, angular):
        twist_stamped = TwistStamped()
        twist_stamped.header.stamp = self.get_clock().now().to_msg()
        twist_stamped.header.frame_id = 'base_link'
        twist_stamped.twist.linear.x = linear[0] * self.linear_speed
        twist_stamped.twist.linear.y = linear[1] * self.linear_speed
        twist_stamped.twist.linear.z = linear[2] * self.linear_speed
        twist_stamped.twist.angular.z = angular[2] * self.angular_speed

        self.publisher_.publish(twist_stamped)
        self.last_key_time = self.get_clock().now()

    def publish_zero_twist(self):
        # Stop publishing if no key press in last 0.5 seconds
        if (self.get_clock().now() - self.last_key_time).nanoseconds > 5e8:
            twist_stamped = TwistStamped()
            twist_stamped.header.stamp = self.get_clock().now().to_msg()
            twist_stamped.header.frame_id = 'base_link'
            self.publisher_.publish(twist_stamped)


def main(args=None):
    global settings
    settings = termios.tcgetattr(sys.stdin)
    rclpy.init(args=args)
    node = TeleopTwistStamped()

    try:
        while rclpy.ok():
            key = get_key()
            if key in move_bindings:
                linear = move_bindings[key]
                angular = (0.0, 0.0, linear[2])
                node.publish_twist(linear, angular)
            elif key in speed_bindings:
                node.linear_speed *= speed_bindings[key]
                node.angular_speed *= speed_bindings[key]
                node.get_logger().info(f"Speed: linear={node.linear_speed:.2f}, angular={node.angular_speed:.2f}")
            elif key == '\x03':  # Ctrl+C
                break

            rclpy.spin_once(node, timeout_sec=0.01)

    except Exception as e:
        node.get_logger().error(f"Exception: {e}")
    finally:
        twist_stamped = TwistStamped()
        twist_stamped.header.stamp = node.get_clock().now().to_msg()
        node.publisher_.publish(twist_stamped)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
