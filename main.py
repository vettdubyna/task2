#!/usr/bin/python

import sys
import os
import time
from scripts.configure_vagrant import *

if __name__ == "__main__":
    try:
        ensure_vagrant()
    except Exception as e:
        print "Error: " + str(e)
        sys.exit(1)