#!/bin/bash

# Up interface
ifup eth1 && echo "Interface has been enabled"

# Install tools
yum -y install wget net-tools

#turn off selinux
sed -i '/SELINUX=enforcing/c \SELINUX=disabled' /etc/selinux/config && echo "selinux disabled"

#disable and stopping firewalld
systemctl stop firewalld.service
systemctl disable firewalld.service
# Enabling forwarding
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf && sysctl -p && echo "ip_forward OK"
