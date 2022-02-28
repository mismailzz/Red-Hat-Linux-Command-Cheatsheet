# Red-Hat-Command-Cheatsheet

The below list are not covering all the commands for Linux Administration. These are commands that are not oftenly used but would be needed extermely in hours of matter of troubleshooting. This list is limited but can be improved much more. 

### Redhat Package Manager

	~$rpm --checksig <.rpm pkg>  # Check RPM signature 
	~$rpm -ivh <.rpm pkg> #install RPM package
	~$rpm -qpR <.rpm pkg> # to check dependencies of RPM package
	~$rpm -ivh --nodeps <.rpm pkg> #install the pkg without dependencies
	~$rpm -ql <.rpm pkg> #List all files of installed RPM packages
	~$rpm -qa  #List installed RPM packages
	~$rpm -q <.rpm pkg> #List installed RPM packages
	~$rpm -qa --last  #List all recently installed RPM packages
	~$rpm -Uvh <.rpm pkg> #Upgrade a RPM package
	~$rpm -evvnx <.rpm pkg> #Remove RPM package
	~$rpm -ev --nodeps #Remove RPM package without dependencies
	~$rpm -qf /usr/bin/htpasswd #Query a file that belongs which RPM package
	~$rpm -qi vsftpd #Show the information of installed RPM package
	~$rpm -qip <.rpm pkg> #Show the information of RPM package before install
	~$rpm -qdf /usr/bin/vmstat #Show documentation of instal RPM package
	~$rpm -Vp <.rpm pkg> #Verifying a package compares information of installed files against rpm db
	~$rpm -Va #Verifying all packages

### YUM (Yellowdog Updater and Modifier)

	~$yum install <pkg>
	~$yum upgrade <pkg>
	~$yum localinsatll <pkg*>
	~$yum remove <pkg/command/rpm>
	~$yum history list #install/update/upgrade or transaction history
	~$yum history list all 
	~$yum history info <id> #pkg info install/update/upgrade or transaction history by id
	~$yum history undo <id> #undo the transaction by id
	~$yum history redo <id> #redo the transaction by id
	~$yum history new #yum stores transaction in single SQLite db. To start new transaction history
	~$yum whatprovides <pkg/command>
	~$yum --showduplicates list httpd | expand
	~$yum list available java*
	~$yum list installed
	

### Permission 

	~$chmod u+s <file> #set suid bit such as -rwsr-xr-x. small s means (rwxs)
	~$chmod 4655 <file> #set suid bit such as -rwSr-xr-x. capital S means (rws)
	~$Setgid on dir, all dir/files in it will get same ownership as parent dir. It doesn't matter who is creating
	~$chmod g+s <dir/file> #setting setgid bit
	~$chmod 1777 <dir> #setting sticky bit such as drwxrwxrwt. small t means (rwxt)
	~$chmod 1776 <dir> #setting sticky bit such as drwxrwxrwT. capital T means (rwt)
	~$chown -R <user>:<group> <dir> #asssigning recursive permission of all files/dir in  target dir

### User Administration 

	~$useradd <user>
	~$useradd -g itadmin -c "DB User" -u 1135 -s "/bin/sh" -d /home/techguy1 
	In the above command, we are creating the new user with custom options as simple "#useradd <user>" will create with default setting. The -g (group) -c (description) -u (user id) -s (which shell to be assigned) -d (landed home dir)
	~$useradd -g <primary group> -G <secondary group> <user> # assign the user primary and secondary group
	~$passwd -l <user> #locking password of user
	~$passwd -u <user> #unlocking password of user
	~$passwd -e <user> #expire password 
	~$echo 'myPassword123' | sudo passwd --stdin <user> 
	~$passwd -x -1 <user> #Turnoff password expiry
	~$usermod -L <user> #locking user
	~$usermod -U <user> #unlocking user
	~$chage #set password expiry

### Access Control Lists (ACLs)

	~$getfacl <file/dir> #to view the access control list of file/dir
	~$setfacl -m u:priya:rw <file> #assiging the a new user 'priya' with read/write permission on the file. -m (modifying) -u (user)
	~$setfacl -m mask:r <file> #setting mask on file
	~$setfacl -d -m u:priya:rw <dir> #setting ACL for directory

### Crontab

	~$crontab -l #show crontab for all users
	~$crontab -u <user> -l #show crontab for specific user
	~$crontab -e #add cron entry in crontab file
 
### Process

	~$ps -a #all terminal 
	~$ps -e #list of all the processes
	~$ps -o #customer properties
	~$ps -ao tty,comm,pid,%mem,%cpu #<command/script> & #run the task in background
	~$ps -fp $(pgrep -d, -x logrotate)
	~$pgrep -u <userid> unison
	~$ps -p <pid> -o etime #process execution time
	~$ps -eo user,pid,ppid,%mem,%cpu --sort=-%cpu | head
	~$ps lax
	~$ps fax

### Network 

	~$dig +trace www.google.com
	~$nmcli dev status
	~$nmcli con del <interface name>
	~$ip addr show <interface name>
	~$nmcli con show
	~$nmcli con add con-name <interface name> type <ethernet> ifname <interface name> ip4 <ip address> gw4 <gateway>
	~$nmcli con up <interface name>
	~$nmcli con mod <interface name> ipv4.gateway <ip address>
	~$hostnamectl set-hostname <hostname>
	~$netstat -rn
	~$route -n
	~$tcpdump -i <interface>
	~$tcpdump -i <interface> host <ipaddress>  -nn
	~$tcpdump -i <interface> -s 0 -w <output file name example.pcap> host <ipaddress/hostname> and udp
	~$ping <hostname/ipaddress>
	~$telnet <hostname/ipaddress> <port>
	~$nslookup <domain/hostname>
	~$netstat -an |grep <ipaddress>.<port>|grep ESTAB|awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -rn #show which remote hosts make how many connection to specfic port, the output is sort on number of connections by host to port 

### Memory/Swap

	~$egrep --color 'Mem|Cache|Swap' /proc/meminfo | awk '{print $1 " " $2/1000/1000 "GB"}' #show information in GB
	~$smem -s swap -t -k -n -r
	~$smem -u -p -r
	~$free -h

### Disk 

	~$df -h
	~$df -Th
	~$du -sh <path/*>
	~$du -sch .[!.]* * | grep --regex="[0-9]*G"
	~$lsof -u <user> #list of openfiles by specific user
	~$lsof | grep delete #list of openfiles that are deleted
	~$lsof | awk '{print $1}' | sort | uniq -c | sort -r -n #sort number of open files by process

### SFTP/SCP
	
	~$sftp -oPort=<port> <user>@<ipaddress/domain>
	~$sftp -oPort=<port> -oIdentityFile=<path to key> <user>@<ipaddress/domain>
	~$sftp -o KexAlgorithms=<keyExchangeAlgo> -o HostKeyAlgorithms=<HostKeyAlgoName> -oIdentityFile=<path to key> -oPort=<port> <user>@<domain/ipaddress>
	~$scp -P <port> <path to src file> <user>@<domain/ipaddress>:<target path> #send the file to target system
	~$scp -P <port> <user>@<domain/ipaddress>:<src file path> <target file path locally> #fetch file from the target system

### Puppet Bolt
	
	~$bolt command run "<command>"  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets @<ipaddress/hostname list file>  -u <user>
	~$bolt command run "<command>"  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets <ipaddress/hostname separate by ,>  -u <user>
	~$bolt script run <script>  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets @<ipaddress/hostname list file>  -u <user>
	~$bolt script run <script>  --no-host-key-check --tmpdir=/tmp -p <password>  --tty --targets <ipaddress/hostname separate by ,>  -u <user>
	
	
### Additional 

	~$top -b -n 1 | head -n +5
	~$uptime
	~$find /tmp/* -mtime +7 -exec rm {} \; #remove files from dir "tmp/" that are older than 7 days 
	~$find /home/ -type f -size +500M -name "*tempfile*" -exec du -sh {} \; #found the tempfile that has file size >500MB
	~$sestatus #check selinux status
	~$sed -n -e "/<$hostname>/,/ismail.com/ p" <targetfile> #replace the string by variable, result will be stdout
	~$sed -i -n -e "/<$hostname>/,/ismail.com/ p" <targetfile> #replace the string by variable, result will be saved in target file
	
	
	

