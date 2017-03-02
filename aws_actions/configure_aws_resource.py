from fabric import *
import boto3
from fabric.operations import sudo
from fabric.context_managers import settings
from fabric.api import env, run
import os
import sys


def preparing_instance(ip_addr, user, key):
    try:
        print "Getting public key..."
        key_to_upload = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
        env['connection_attempts'] = 100
        env.key_filename = [key]
        env.host_string = user + '@' + ip_addr
        print "Deploying public key..."
        run('echo "%s" > ~/.ssh/authorized_keys' % key_to_upload)
        run('chmod 644 ~/.ssh/authorized_keys')
        run('chmod 700 ~/.ssh/')
        return True
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)
