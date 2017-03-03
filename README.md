## Python custom task 2
### Tasks list
#### Environment configuration
1. Build two VMs on your PC:
	*CentOS based router with two network interfaces.
		- one is for internet connection;
	   	- second (IP 172.17.168.1) is only for internal use for host range: 172.17.160.1 - 172.17.175.25
	*Ubuntu_VM based with one network interface
		- IP 172.17.175.175
		- SSH access configured

2. Run your Amazon Linux instance: OS does not matter. This instanse used as internet access hub to your local Ubuntu_VM.

#### Network configuration
1. Write bash script with can be run from any system connected to internet:
  1) secure connect to Ubuntu_VM
  2) create lvm volume 1G and mount it to /mnt/<YOURNAME>
  3) create ten 1MB zero-filled files in /mnt/<YOURNAME> with random names
  4) create user tstuser and add him to root group
  5) grant additional RW rights to tstuser for created files.
  6) display Ubuntu_VM IP,MAC, tstuser group assignment and /mnt/<YOURNAME>
  7) filelsit
  8) remove lvm volume
