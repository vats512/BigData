#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")
    key = str(entry[14])+","+str(entry[16])
    value = 1
    print(key+"\t"+str(value))
