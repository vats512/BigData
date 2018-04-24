#!/usr/bin/env python
import sys
import string
from csv import reader
for line in sys.stdin:
    row = reader([line])
    entry = (list(row)[0])
    if(len(entry) == 18):
    	print(str(entry[2])+"\t"+str(entry[12]))

