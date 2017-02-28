# task2
=Build two VMs on your PC:

  1) CentOS based router with two network interfaces.
	   - one is for internet connection;
	   - second (IP 172.17.168.1) is only for internal use for host range:
		 172.17.160.1 - 172.17.175.254
   2) Ubuntu_VM based with one network interface
		 - IP 172.17.175.175
		- SSH access configured

=Run your Amazon Linux instance:
   OS does not matter.
	This instanse used as internet access hub to your local Ubuntu_VM.


#### Network configuration

=Write bash script with can be run from any system connected to internet:
   - secure connect to Ubuntu_VM
   - create lvm volume 1G and mount it to /mnt/<YOURNAME>
   - create ten 1MB zero-filled files in /mnt/<YOURNAME> with random names
   - create user tstuser and add him to root group
   - grant additional RW rights to tstuser for created files.
	- display Ubuntu_VM IP,MAC, tstuser group assignment and /mnt/<YOURNAME>
 filelsit
   - remove lvm volume
