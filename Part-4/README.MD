# Part 4:

#### ROS Discovery server on host computer

Here we will use husarnet ros_discovery_server on our own pc. For this you need to connect to your husarnet network as talked about in part 1.

After that when running any type of ros node, run the following commands.

```
fastdds discovery -i 0 -l husarnet-local -p 11811
```

to run the discovery server.

Now we can run the demo nodes as follows

```
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
export ROS_SUPER_CLIENT=TRUE
export ROS_DISCOVERY_SERVER=husarnet-local:11811

ros2 run demo_nodes_cpp talker
```

and

```
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
export ROS_SUPER_CLIENT=TRUE
export ROS_DISCOVERY_SERVER=husarnet-local:11811

ros2 run demo_nodes_cpp listener
```

Now if you try to list the ROS2 Topics, you will still not find the chatter topic. For that,
make sure you are in the directory of the following file to setup SuperClient. Then run
```
export FASTRPS_DEFAULT_PROFILES_FILE=superclient.xml
```
You might have to reboot ROS2 daemon as follows in case it doesnt work immediately

```
ros2 daemon stop
ros2 daemon start
```

then run 

```
ros2 topic list
```

you will be able to see the /chatter topic.