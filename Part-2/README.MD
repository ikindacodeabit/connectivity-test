# Part 2:

## Pinging

To join a network, 

```
sudo husarnet join fc94:...:932a/XXXXXXXXXXXXXXXXXXXXX mylaptop
```

where mylaptop is the name of device on the network.

XXX... - joincode of the network.

After joining, you can ping any device on the network by

```
ping6 mylaptop
```

You can also join SSH-able devices using the following command 

```
ssh username@mylaptop
```
