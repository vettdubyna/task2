#!/usr/bin/python

import sys
import os
import io
import ConfigParser

from menu_functions.prepare import *
from scripts.configure_vagrant import *
from scripts.boxes_actions import *
from aws_actions.create_aws_resource import *
from aws_actions.get_aws_resource import *
from aws_actions.clear_aws_resources import *
from aws_actions.configure_aws_resource import *

if False: #__name__ == "__main__":
    ec2_params = {}
    ec2_id = ""
    ec2_ip = ""
    host_name = "host"
    router_name = "router"
    try:
        ec2_params = set_params("config/configuration.ini")
        print_headers("Configuring virtualization")
        ensure_env()
        print_headers("Define IP-address")
        if define_ip():
            print "IP-address has been changed"
        else:
            print "IP-address has been set by default"

        print_headers("Create EC2 instance")
        try:
            ec2_id = create_ec2_instance(ec2_params)
            ec2_ip = get_ec2_ip(ec2_id)
            preparing_instance(ec2_ip, "ubuntu", "keys/" + ec2_params["key_name"] + ".pem")
            print ec2_ip, ec2_id
        except Exception as e:
            print "Error: " + str(e)
            terminate_ec2(ec2_id)
            sys.exit(1)

        print_headers("Create boxes")
        try:
            print "Creating router..."
            create_vagrant_box(router_name, "source/router/Vagrantfile", "scripts/configure_router.sh")
            print "Creating machine..."
            create_vagrant_box(host_name, "source/machine/Vagrantfile", "scripts/configure_machine.sh")
        except Exception as e:
            print "Error: " + str(e)
            terminate_ec2(ec2_id)
            clear_box(host_name)
            clear_box(router_name)
            sys.exit(1)

    except Exception as e:
        print "Error: " + str(e)
        terminate_ec2(ec2_id)
        clear_box(host_name)
        clear_box(router_name)
        sys.exit(1)


clear_box("machine")
clear_box("router")