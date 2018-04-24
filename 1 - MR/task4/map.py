#!/usr/bin/env python

import sys
import string
from csv import reader
for line in sys.stdin:
    row = reader([line])
    entry = (list(row)[0])
    if(len(entry) == 22):
	    key = str(entry[16])
	    if key == "NY":
	    	print("NY"+"\t"+"1")
	    else:
	    	print("Other"+"\t"+"1")

