#!/usr/bin/env python

import sys
import string
from csv import reader
for line in sys.stdin:
    row = reader([line])
    entry = (list(row)[0])
    if(len(entry) == 22):
	    key = str(entry[2])
	    value = str(entry[1])
	    dates = value.strip().split("-")
	    date = int(dates[2])
	    print(key+"\t"+str(date))
