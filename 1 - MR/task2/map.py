#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")
    print(str(entry[2])+"\t"+str(1))

