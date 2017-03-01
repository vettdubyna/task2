import os

import sys
import shutil

def create_vagrant_box(machine, vfile, script):
    try:
        #copy Vagrantfile and script to dest. dir
        cwd = os.getcwd()
        directory = cwd + "/../vagrant/" + machine
        os.mkdir(directory, mode=0755)
        shutil.copy2(vfile, directory + "/")
        shutil.copy2(script, directory + "/script.sh")

        #run vagrant box
        os.system("export VAGRANT_CWD=" + directory)
        os.system("vagrant up --provision")
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)
