#!/bin/bash
set -e

# Source ROS setup
source /opt/ros/jazzy/setup.bash
source /ros2_ws/src/install/setup.bash

exec "$@"

