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
	~$yum history list #install/update/upgrade or transaction history
	~$yum history list all 
	~$yum history info <id> #pkg info install/update/upgrade or transaction history by id
	~$yum history undo <id> #undo the transaction by id
	~$yum history redo <id> #redo the transaction by id
	~$yum history new #yum stores transaction in single SQLite db. To start new transaction history


### Permission 

	~$chmod u+s <file> #set suid bit such as -rwsr-xr-x. small s means (rwxs)
	~$chmod 4655 <file> #set suid bit such as -rwSr-xr-x. capital S means (rws)
	~$Setgid on dir, all dir/files in it will get same ownership as parent dir. It doesn't matter who is creating
	~$chmod g+s <dir/file> #setting setgid bit
	~$chmod 1777 <dir> #setting sticky bit such as drwxrwxrwt. small t means (rwxt)
	~$chmod 1776 <dir> #setting sticky bit such as drwxrwxrwT. capital T means (rwt)
	~$chown -R <user>:<group> <dir> #asssigning recursive permission of all files/dir in  target dir

### User Administration 

	~$useradd -g itadmin -c "DB User" -u 1135 -s "/bin/sh" -d /home/techguy1 
	In the above command, we are creating the new user with custom options as simple "#useradd <user>" will create with default setting. The -g (group) -c (description) -u (user id) -s (which shell to be assigned) -d (landed home dir)
	~$useradd -g <primary group> -G <secondary group> <user> # assign the user primary and secondary group
	~$passwd -l <user> #locking password of user
	~$passwd -u <user> #unlocking password of user
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
	~$ps -ao tty,comm,pid,%mem,%cpu
	•  #<command/script> & #run the task in background

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
