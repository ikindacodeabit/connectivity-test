FROM osrf/ros:jazzy-desktop-full

RUN apt update && apt install -y \
        ros-${ROS_DISTRO}-demo-nodes-cpp && \
        ros-${ROS_DISTRO}-rviz2 \
        x11-apps \
    && rm -rf /var/lib/apt/lists/*