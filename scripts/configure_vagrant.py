import os

import sys


def ensure_vagrant():
    try:
        os.system("wget -o https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1_x86_64.deb")
        os.system("sudo dpkg -i vagrant_1.9.1_x86_64.deb")
        os.system("sudo rm -rf vagrant_1.9.1_x86_64.deb")
        os.system("vagrant box add centos/7")
        os.system("vagrant box add ubuntu/trusty64")
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)