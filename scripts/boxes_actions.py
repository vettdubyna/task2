import os

import sys
import shutil
from menu_functions.prepare import *


def create_vagrant_box(host, vfile, scripts_path):
    try:
        #copy Vagrantfile and script to dest. dir
        cwd = os.getcwd()
        directory = cwd + "/vagrant/" + host + "/"
        print "Current dir is: " + directory
        os.system("mkdir -p " + directory)
        shutil.copy2(vfile, directory)
        generate_unique_script(scripts_path, directory + "script.sh")

        #run vagrant box
        os.environ['VAGRANT_CWD'] = directory
        os.system("vagrant up --provision")
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)


def clear_box(host):
    try:
        cwd = os.getcwd()
        directory = cwd + "/vagrant/" + host
        print directory
        os.environ['VAGRANT_CWD'] = directory + "/"
        os.system("vagrant halt; vagrant destroy -f")
        os.system("rm -rf " + directory)
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)
