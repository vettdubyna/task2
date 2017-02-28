#!/usr/bin/python

import sys
import os
import time
from scripts.configure_vagrant import *


def print_headers(str):
    print " ====================== " + str + " ====================== "

if __name__ == "__main__":
    try:
        print_headers("Configuring virtualization")
        ensure_env()

    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)