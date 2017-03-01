#!/usr/bin/python

import boto3
import sys

def get_ec2_ip(instance_id):
    try:
        ec2 = boto3.resource('ec2')
        instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-id', 'Values': [instance_id]}])
        for instance in instances:
            return getattr(instance, 'public_dns_name')
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)