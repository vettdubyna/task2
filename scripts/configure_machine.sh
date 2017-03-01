#!/bin/bash

#add default gateway
route add default gw 172.17.168.1 eth1
route delete default dev eth0

#open 5555 port for ssh
sed -i '/Port 5555\c /Port 5555' /etc/ssh/sshd_config || sed -i '/Port\a /Port 5555' /etc/ssh/sshd_config
