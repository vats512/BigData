#!/usr/bin/env python

import sys
import string
from csv import reader
for line in sys.stdin:
    row = reader([line])
    entry = (list(row)[0])
    if(len(entry) == 22):
	    key = str(entry[14])+","+str(entry[16])
	    value = 1
	    print(key+"\t"+str(value))
