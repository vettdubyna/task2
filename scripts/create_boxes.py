import os

import sys
import shutil

def create_vagrant_box(machine, vfile, script):
    try:
        #copy Vagrantfile and script to dest. dir
        cwd = os.getcwd()
        directory = cwd + "/vagrant/" + machine + "/"
        print directory
        os.system("mkdir -p " + directory)
        shutil.copy2(vfile, directory)
        shutil.copy2(script, directory + "script.sh")

        #run vagrant box
        os.environ['VAGRANT_CWD'] = directory
        os.system("vagrant up --provision")
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)
