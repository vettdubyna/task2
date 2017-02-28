#!/usr/bin/python

import sys
import os
import time

if __name__ == "__main__":
    try:
        print "Hello"
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)