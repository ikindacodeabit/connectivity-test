# Part 1:

## Installing Husarnet on Linux

Use this command to install the CLI:
```
curl -s https://install.husarnet.com/install.sh | sudo bash
```

## About the Client

On using husarnet status (use husarnet status -v for more info)you might see the following :
```
$ husarnet status  
Version  
🟢 CLI: 2022.10.20.2  
🟢 Daemon (running): 2022.10.20.2  
🟢 Daemon (binary): 2022.10.20.2  
  
Dashboard URL  
🟢 CLI: app.husarnet.com  
🟢 Daemon: app.husarnet.com  
  
Connection status  
🟢 Base Server: 188.165.23.196:5582 (UDP)  
  
Readiness  
🟢 Is ready to handle data? yes  
🟢 Is ready to join? yes  
🟢 Is joined? yes  
  
Local  
⚪ Husarnet IP:  
fc94:d797:bcdf:d20a:e2dc:c25e:2536:c1cd  
  
Whitelist  
fc94:41c9:86b6:7570:897f:b86f:7b5b:9818 husarnet-win11  
⚪ inactive 🟢 secure 🟡 tunelled  
  
fc94:b01d:1803:8dd8:b293:5c7d:7639:932a (websetup)  
⚪ inactive 🟢 secure 🟡 tunelled  
  
fc94:cff2:8a4b:0197:50cd:0b08:14ac:cc7b aws-test-husarnet  
⚪ inactive 🟢 secure 🟡 tunelled  
  
fc94:d797:bcdf:d20a:e2dc:c25e:2536:c1cd (localhost) gnaarmok  
⚪ inactive ⚪ no data flow 🟡 tunelled
```

```
🟢 Base Server: 188.165.23.196:5582 (UDP)
```
is the first choice and then 
```
Connection status  
🟡 Base Server: 188.165.23.196:443 (TCP)  
🟡 TCP is a fallback connection method. You'll get better results on UDP
```
is the fallback second choice.

To manage whitelist :

```
husarnet daemon whitelist ls
```

To add/remove IPv6 addresses, use following commands:

```
husarnet daemon whitelist add <IPv6_address>  
husarnet daemon whitelist rm <IPv6_address
```


To show all device groups :

```
husarnet dashboard group ls
```

for more details use:

```
husarnet dashboard group show <ID>
```

To rename dashboard group :

```
husarnet dashboard group rename "my old group" "my new group"
```

To see all devices assigned to your account :

```
husarnet dashboard device ls
```

To assign a device:

```
husarnet dashboard assign
```
 
 and to unassign:

 ```
 husarnet dashboard unassign
```

In one command we can use:

```
husarnet dashboard assign <DEVICE_NAME> <GROUP_NAME>
```
