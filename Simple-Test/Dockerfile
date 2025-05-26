FROM ros:jazzy-ros-core

# Install build tools
RUN apt update && apt install -y \
    python3-colcon-common-extensions \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set up workspace
RUN mkdir -p /ros2_ws/src
WORKDIR /ros2_ws

# Copy source code for chatter build
COPY ./src /ros2_ws/src

# Build the workspace
RUN /bin/bash -c "source /opt/ros/jazzy/setup.bash && colcon build --symlink-install"

# Add entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

