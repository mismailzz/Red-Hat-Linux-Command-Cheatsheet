# CentOS/Red-Hat-Command-Cheatsheet

The below list are not covering all the commands for Linux Administration. These are commands that are not oftenly used but would be needed extermely in hours of matter of troubleshooting. This list is limited but can be improved much more. 

<details><summary>Redhat Package Manager (RPM)</summary>
<p>

```bash   
#Check RPM signature  
rpm --checksig <.rpm pkg>
```
```bash
#Install RPM package
rpm -ivh <.rpm pkg> 
```
```bash
#Check dependencies of RPM pkg 
rpm -qpR <.rpm pkg> 
```
```bash
#Install RPM pkg without dependencies
rpm -ivh --nodeps <.rpm pkg>  
```
```bash
#List all files of installed RPM packages
rpm -ql <.rpm pkg> 
```
```bash
#List installed RPM packages
rpm -qa  
```
```bash
#List installed RPM packages
rpm -q <.rpm pkg> 
```
```bash
#List all recently installed RPM packages
 rpm -qa --last  
```
```bash
#Upgrade a RPM package
rpm -Uvh <.rpm pkg> 
```
```bash
#Remove RPM package 
rpm -evvnx <.rpm pkg> 
```
```bash
#Remove RPM package without dependencies 
rpm -ev --nodeps 
```
```bash
#Query a file that belongs which RPM package 
rpm -qf /usr/bin/htpasswd 
```
```bash
#Show the information of installed RPM package 
rpm -qi vsftpd 
```
```bash
#Show the information of RPM package before install 
rpm -qip <.rpm pkg> 
```
```bash
#Show documentation of instal RPM package 
rpm -qdf /usr/bin/vmstat 
```
```bash
#Verifying a package compares information of installed files against rpm db 
rpm -Vp <.rpm pkg> 
```
```bash
#Verifying all packages 
rpm -Va 
```
</p>
</details>
  
<details><summary>YUM (Yellowdog Updater and Modifier)</summary>
<p>

```bash
yum upgrade <pkg>

```
```bash
yum localinsatll <pkg*>

```
```bash
yum remove <pkg/command/rpm>

```
```bash
#install/update/upgrade or transaction history
yum history list 

```
```bash
yum history list all 

```
```bash
#pkg info install/update/upgrade or transaction history by id
yum history info <id> 

```
```bash
#undo the transaction by id
yum history undo <id> 

```
```bash
#redo the transaction by id
yum history redo <id> 

```
```bash
#yum stores transaction in single SQLite db. To start new transaction history
yum history new 

```
```bash
yum whatprovides <pkg/command>

```
```bash
yum --showduplicates list httpd | expand

```
```bash
yum list available java*

```
```bash
yum list installed

```
</p>
</details>  


 <details><summary>Permission </summary>
<p>

```bash
#set suid bit such as -rwSr-xr-x. capital S means (rws)
chmod 4655 <file> 

```
```bash
#Setgid on dir, all dir/files in it will get same ownership as parent dir. It doesn't matter who is creating
```
```bash
#setting setgid bit
chmod g+s <dir/file> 
```
```bash
#setting sticky bit such as drwxrwxrwt. small t means (rwxt)
chmod 1777 <dir> 
```
```bash
#setting sticky bit such as drwxrwxrwT. capital T means (rwt)
chmod 1776 <dir> 
```
```bash
#asssigning recursive permission of all files/dir in  target dir
chown -R <user>:<group> <dir> 
```
</p>
</details>
  
  
<details><summary>User Administration</summary>
<p>

```bash
useradd -g itadmin -c "DB User" -u 1135 -s "/bin/sh" -d /home/techguy1 
#In the above command, we are creating the new user with custom options as simple "#useradd <user>" will create with default setting. The -g (group) -c (description) -u (user id) -s (which shell to be assigned) -d (landed home dir)
```
```bash
useradd -g <primary group> -G <secondary group> <user> # assign the user primary and secondary group

```
```bash
passwd -l <user> #locking password of user

```
```bash
passwd -u <user> #unlocking password of user

```
```bash
passwd -e <user> #expire password 

```
```bash
echo 'myPassword123' | sudo passwd --stdin <user> 

```
```bash
passwd -x -1 <user> #Turnoff password expiry

```
```bash
usermod -L <user> #locking user

```
```bash
usermod -U <user> #unlocking user

```
```bash
chage #set password expiry

```

</p>
</details>
 

<details><summary>Access Control Lists (ACLs)</summary>
<p>

```bash
setfacl -m u:priya:rw <file> #assiging the a new user 'priya' with read/write permission on the file. -m (modifying) -u (user)
```
```bash
setfacl -m mask:r <file> #setting mask on file
```
```bash
setfacl -d -m u:priya:rw <dir> #setting ACL for directory
```

</p>
</details>


<details><summary>Crontab</summary>
<p>

```bash
crontab -l #show crontab for all users
```
```bash
crontab -u <user> -l #show crontab for specific user
```
```bash
crontab -e #add cron entry in crontab file
```

</p>
</details>


<details><summary>Process</summary>
<p>

```bash
ps -a #all terminal 
```
```bash
ps -e #list of all the processes
```
```bash
ps -o #customer properties

```
```bash
ps -ao tty,comm,pid,%mem,%cpu #<command/script> & #run the task in background

```
```bash
ps -fp $(pgrep -d, -x logrotate)

```
```bash
pgrep -u <userid> unison

```
```bash
ps -p <pid> -o etime #process execution time

```
```bash
ps -eo user,pid,ppid,%mem,%cpu --sort=-%cpu | head

```
```bash
ps lax

```
```bash
ps fax

```


</p>
</details>


<details><summary>Network</summary>
<p>


```bash
dig +trace www.google.com

```
```bash
nmcli dev status

```
```bash
nmcli con del <interface name>

```
```bash
ip addr show <interface name>

```
```bash
nmcli con show

```
```bash
nmcli con add con-name <interface name> type <ethernet> ifname <interface name> ip4 <ip address> gw4 <gateway>

```
```bash
nmcli con up <interface name>

```
```bash
nmcli con mod <interface name> ipv4.gateway <ip address>

```
```bash
hostnamectl set-hostname <hostname>

```
```bash
netstat -rn

```
```bash
route -n

```
```bash
tcpdump -i <interface>

```
```bash
tcpdump -i <interface> host <ipaddress>  -nn

```
```bash
tcpdump -i <interface> -s 0 -w <output file name example.pcap> host <ipaddress/hostname> and udp

```
```bash
ping <hostname/ipaddress>

```
```bash
telnet <hostname/ipaddress> <port>

```
```bash
nslookup <domain/hostname>

```
```bash
netstat -an |grep <ipaddress>.<port>|grep ESTAB|awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -rn #show which remote hosts make how many connection to specfic port, the output is sort on number of connections by host to port 

```

</p>
</details>


<details><summary>Memory</summary>
<p>


```bash
egrep --color 'Mem|Cache|Swap' /proc/meminfo | awk '{print $1 " " $2/1000/1000 "GB"}' #show information in GB

```
```bash
smem -s swap -t -k -n -r

```
```bash
smem -u -p -r

```
```bash
free -h

```

</p>
</details>


<details><summary>Disk</summary>
<p>

```bash
df -h

```
```bash
df -Th

```
```bash
du -sh <path/*>

```
```bash
du -sch .[!.]* * | grep --regex="[0-9]*G"

```
```bash
lsof -u <user> #list of openfiles by specific user

```
```bash
lsof | grep delete #list of openfiles that are deleted

```
```bash
lsof | awk '{print $1}' | sort | uniq -c | sort -r -n #sort number of open files by process

```

</p>
</details>


<details><summary>SFTP/SCP</summary>
<p>

```bash
sftp -oPort=<port> <user>@<ipaddress/domain>

```
```bash
sftp -oPort=<port> -oIdentityFile=<path to key> <user>@<ipaddress/domain>

```
```bash
sftp -o KexAlgorithms=<keyExchangeAlgo> -o HostKeyAlgorithms=<HostKeyAlgoName> -oIdentityFile=<path to key> -oPort=<port> <user>@<domain/ipaddress>

```
```bash
sftp -oPort=<port> -o KexAlgorithms=diffie-hellman-group14-sha1 -o HostKeyAlgorithms=+ssh-dss -oIdentityfile=<path to key> <user>@<domain/ipaddress>

```
```bash
scp -P <port> <path to src file> <user>@<domain/ipaddress>:<target path> #send the file to target system

```
```bash
scp -P <port> <user>@<domain/ipaddress>:<src file path> <target file path locally> #fetch file from the target system

```

</p>
</details>


<details><summary>Bolt</summary>
<p>

<i>For the --tmpdir flag we can use the home directory path of the remote user which will logged in on the behalf of the bolt. At some time /tmp is not executable due to which the command gets failed. (~mizz - will be confirm) </i>

```bash
bolt command run "<command>"  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets @<ipaddress/hostname list file>  -u <user>

```
```bash
bolt command run "<command>"  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets <ipaddress/hostname separate by ,>  -u <user>

```
```bash
bolt script run <script>  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets @<ipaddress/hostname list file>  -u <user>

```
```bash
bolt script run <script>  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets <ipaddress/hostname separate by ,>  -u <user>

```

</p>
</details>


<details><summary>Sed</summary>
<p>

```bash
sed -n -e "/<$hostname>/,/ismail.com/ p" <targetfile> #replace the string by variable, result will be stdout

```
```bash
sed -i -n -e "/<$hostname>/,/ismail.com/ p" <targetfile> #replace the string by variable, result will be saved in target file

```
```bash
sed -i 's/stringtoreplace/newstring/g' myfile.txt #replace the string from the file globally

```

</p>
</details>


<details><summary>find</summary>
<p>

```bash
find /tmp/* -mtime +7 -exec rm {} \; #remove files from dir "tmp/" that are older than 7 days 

```
```bash
find /home/ -type f -name ".errors*.gz" -mtime +7 -exec rm {} \; #remove files from dir "tmp/" that are older than 7 days - with filename

```
```bash
find /home/ -type f -size +500M -name "*tempfile*" -exec du -sh {} \; #found the tempfile that has file size >500MB

```
```bash
find /home/ -type f -size +1G -exec ls -lh {} \; | awk '{ print $9 "|| Size : " $5 }' #find output in custom defined format like in this "dirname || Size:_"

```

</p>
</details>


<details><summary>grep</summary>
<p>


```bash
cat myfile | grep -B 1 -A 4 -i 'string one\|string two' #it will show 1 line before and 4 lines after matching the strings form myfile

```
```bash
grep -lr "string" * #search recursively the string from all filesystem hierarchy, as its start from which current dir you are standing and it will list files

```
```bash
grep -ir "string" <* or file> #search recursively the string from all filesystem hierarchy and show the content what matches - * for all files otherwise specify a single file

```

</p>
</details>


<details><summary>Other</summary>
<p>

```bash
top -b -n 1 | head -n +5

```
```bash
uptime

```
```bash
sestatus #check selinux status

```

</p>
</details>

  
