## Simple Test

This simple test is to show how you can run your own code.
Here we accomplish the following :
- Mounting custom code in docker, with this we can work on our code separately and then easily access it in the docker container.
- We connect successfully over Husarnet using the the ROS DISCOVERY SERVER
- It also shows how to pass commands directly to the container to run on start-up

You can use the same commands from the previous part in separate terminals:

```
docker compose -f compose.ds.yaml up
```

```
CHATTER_ROLE=talker docker compose up
```

```
CHATTER_ROLE=listener docker compose up
```

For SuperClient:
```
docker compose -f compose.superclient.yaml up
```