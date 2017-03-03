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
        private_key = open(os.path.expanduser('~/.ssh/id_rsa')).read()
        public_key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
        env['connection_attempts'] = 100
        env.key_filename = [key]
        env.host_string = user + '@' + ip_addr
        print "Deploying public key..."
        run('echo "%s" > ~/.ssh/authorized_keys' % public_key)
        run('echo "%s" > ~/.ssh/id_rsa' % private_key)
        run('echo "%s" > ~/.ssh/id_rsa.pub' % public_key)
        run('chmod 700 ~/.ssh')
        run('chmod 600 ~/.ssh/*')
        run('chmod 644 ~/.ssh/authorized_keys')
        return True
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)
