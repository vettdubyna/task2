import os

import sys


def ensure_virtualbox(password):
    try:
        if os.popen("VBoxManage --version 2> /dev/null").read() != "":
            print "Virtual Box already exists on your system!"
            return True
        else:
            print "Virtual Box doesn't exists on your system!"
            if raw_input("Do you want to install virtual box from script? (yes/no)") == "yes":
                os.system("echo %s | sudo -S apt-get install virtualbox" % password)
                return True
            else:
                return False
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)


def ensure_vagrant(password):
    try:
        if os.popen("vagrant --version 2> /dev/null").read() == "":
            print "Installing vagrant on your system..."
            os.system("wget https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1_x86_64.deb")
            os.system("echo %s | sudo -S dpkg -i vagrant_1.9.1_x86_64.deb" % password)
            os.system("rm -rf vagrant_1.9.1_x86_64.deb")
        print "Vagrant already exists on your system!"
        print "Adding boxes..."
        os.system("vagrant box add centos/7")
        os.system("vagrant box add ubuntu/trusty64")
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)


def ensure_env():
    try:
        password = raw_input("Please enter your root password: ")
        if ensure_virtualbox(password):
            ensure_vagrant(password)
        else:
            print "Please install virtual box manually and rerun the script"
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)