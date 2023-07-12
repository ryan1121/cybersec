#Hack The Box Notes

[toc]

## ping
**'ping'** command is use to check the connection quality.
We don't need to run for a long time. Sometimes, getting a snippet of the result or an overviem instead of a detailed report is more time-efficient than the alternative.
```
ping 10.129.136.187
```

## nmap
**'nmap'** is use to scan the IP address for any open ports and service
### -sV
**'-sV'** param is the appropriate service version detection switch
We can use this param to get more detailed information of any open ports and services.
```
nmap -sV {target_IP}
```

### -p
**'-p'** param can help us to specify the port number when scanning
### Single-Port Scan
```
nmap -p 973 {target_IP}
```
### TCP Connection Scan
```
nmap -p T:7777, 973 {target_IP}
```
### A range of port scan
Using hyphens to separate a range of ports:
```
nmap -p 6300-700 {target_IP}
```

## smbclient
**smbclient** is a command-line utility that provides an FTP-like interface for accessing SMB/CIFS resources on servers. 
SMB/CIFS (Server Message Block/Common Internet File System) is a network protocol used for sharing files, printers, and other resources between computers on a network.
- Allows us to browse and access shared folders and files on remote servers that use the SMB/CIFS protocol. 
1. Connect to a share (user will be prompted for password; `exit` to quit the session):
```
smbclient //server/share
```

2. Connect with a different username:
```
smbclient //server/share --user username
```

3. Connect with a different workgroup:
```
smbclient //server/share --workgroup domain --user username
```

4. Connect with a username and password:
```
smbclient //server/share --user username%password
```

