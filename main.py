#!/usr/bin/python

import sys
import os
import io
import ConfigParser

from menu_functions.prepare import *
from scripts.configure_vagrant import *
from scripts.create_boxes import *
from aws_actions.create_aws_resource import *
from aws_actions.get_aws_resource import *
from aws_actions.clean_aws_resources import *
from aws_actions.configure_aws_resource import *

if __name__ == "__main__":
    try:
        ec2_params = {}
        ec2_id = ""
        ec2_ip = ""
        ec2_params = set_params("config/configuration.ini")
        print_headers("Configuring virtualization")
        ensure_env()
        print_headers("Define IP-address")
        if define_ip():
            print "IP-address has been changed"
        else:
            print "IP-addess has been setted by default"

        print_headers("Create EC2 instance")
        ec2_id = create_ec2_instance(ec2_params)
        ec2_ip = get_ec2_ip(ec2_id)
        preparing_instance(ec2_ip, "ubuntu", "keys/" + ec2_params["key_name"] + ".pem")
        print ec2_ip, ec2_id
        print_headers("Create boxes")
        print "Creating router..."
        create_vagrant_box("router", "source/router/Vagrantfile", "scripts/configure_router.sh")

        print "Creating machine..."
        create_vagrant_box("machine", "source/machine/Vagrantfile", "scripts/configure_machine.sh")

    except Exception as e:
        print "Error: " + str(e)
        terminate_ec2(ec2_id)
        sys.exit(1)