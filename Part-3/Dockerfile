FROM osrf/ros:jazzy-desktop-full

RUN apt update && apt install -y \
        ros-${ROS_DISTRO}-demo-nodes-cpp && \
    rm -rf /var/lib/apt/lists/*