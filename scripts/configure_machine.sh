#!/bin/bash

#add default gateway
route add default gw 172.17.168.1 eth1
route delete default dev eth0

