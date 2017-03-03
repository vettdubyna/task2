#!/usr/bin/env bash

## FIREWALL ##

# Here is the place to define some variables
publicaddr="10.0.2.15"
privateaddr="172.17.168.1"
any="0.0.0.0/0"
localnet="172.17.175.175"

#First, flushing the existing rules
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
iptables -F -t nat
echo "flush OK"

#Now defining the standard policy
#iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
echo "default OK"

#Defining the real stuff !

# Allow access to the firewall from the localnet
iptables -A INPUT -s $localnet -d $privateaddr -j ACCEPT
iptables -A INPUT -s $localnet -d $publicaddr -j ACCEPT
echo "firewall to localhost OK"

# Allow access from ourself to us !
iptables -A INPUT -i lo -j ACCEPT
echo "lo OK"

# Allow the firewall box to access the internet
iptables -A INPUT -s $any -d $publicaddr -m state --state ESTABLISHED,RELATED -j ACCEPT
echo "established OK"

# masquerade the localnet to internet
iptables -t nat -A POSTROUTING -s $localnet -d $any -j MASQUERADE
#iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
echo "masq OK"

#iptables-save #preup
systemctl restart NetworkManager.service