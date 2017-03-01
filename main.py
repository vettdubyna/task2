#!/usr/bin/python

import sys
import os
import io
import ConfigParser

from menu_functions.prepare import *
from scripts.configure_vagrant import *


if __name__ == "__main__":
    try:
        ec2_params = {}
        ec2_params = set_params("config/configuration.ini")
        print_headers("Configuring virtualization")
        #ensure_env()
        print_headers("Define IP-address")
        if define_ip():
            print "IP-address has been changed"
        else:
            print "IP-addess has been setted by default"

    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)