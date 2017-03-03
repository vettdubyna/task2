from fabric import *
import boto3
from fabric.operations import sudo
from fabric.context_managers import settings
from fabric.api import env, run
import os
import sys


def terminate_ec2(id):
    try:
        ec2 = boto3.resource('ec2')
        print "Terminating instance..."
        ids = []
        ids.append(id)
        print ids
        ec2.instances.filter(InstanceIds=ids).stop()
        ec2.instances.filter(InstanceIds=ids).terminate()
        print "Instance has been terminated!"
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)