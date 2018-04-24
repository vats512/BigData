#!usr/bin/env python

import sys
from csv import reader

for line in sys.stdin:
    row = reader([line])
    entry = list(row)[0]
    if len(entry) == 22:
    	make = str(entry[20])
        color = str(entry[19])
        if make == "":
        	print("a00 NONE\t1")
        else:
        	print("a00 "+make+"\t1")
        if color == "":
        	print("b11 NONE\t1")
        else:
        	print("b11 "+color+"\t1")

