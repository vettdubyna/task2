#!/usr/bin/python
import ConfigParser

import io

import sys

import re

import os


def set_params(path):
    try:
        params = {}
        with open(path) as f:
            sample_conf = f.read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(sample_conf))
        for section in config.sections():
            for options in config.options(section):
                params[options] = config.get(section, options)
        return params
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)


def print_headers(str):
    print " ====================== " + str + " ====================== "


def replace_text_in_file(file_name, old, new, count):
    try:
        with open(file_name, 'r') as f:
            filedata = f.read()

        # Replace the target string
        filedata = filedata.replace(old, new, count)

        # Write the file out again
        with open(file_name, 'w') as f:
            f.write(filedata)
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)


def define_ip():
    try:
        if raw_input("The default ip for host is 172.17.175.175. Would you like to change it? (yes/no): ") == "yes":
            ip_machine = raw_input("Please enter new IP-address: ")
            pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
            if not pat.match(ip_machine):
                return False
            else:
                lst = ip_machine.split(".")
                ip_router = lst[0] + "." + lst[1] + "." + lst[2] + "." + "1"

                # change ip-adresses in Vagrantfiles
                replace_text_in_file("source/host/Vagrantfile", "172.17.175.175", ip_machine, 1)
                replace_text_in_file("source/router/Vagrantfile", "172.17.168.1", ip_router, 1)

                # change ip-adresses in bash scripts
                replace_text_in_file("scripts/configure_host.sh", "172.17.168.1", ip_router, 1)
                replace_text_in_file("scripts/configure_router.sh", "172.17.168.1", ip_router, 1)
                replace_text_in_file("scripts/configure_router.sh", "172.17.175.175", ip_machine, 1)
                print ip_machine + "\n" + ip_router
            return True
        else:
            return False
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)


# Function for creating the unique script from a box of scripts
def generate_unique_script(path_to_scripts, result_path):
    try:
        scripts = []
        for file in os.listdir(path_to_scripts):
            if file.endswith(".sh"):
                scripts.append(os.path.join(path_to_scripts, file))
        result_script = ""
        for script in scripts:
            with open(script, 'r') as f:
                tmp = f.read()
                result_script += tmp + "\n"
        with open(result_path, 'w+') as f:
            f.write(result_script)
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)
