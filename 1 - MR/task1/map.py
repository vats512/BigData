#!/usr/bin/env python
import sys
import string
from csv import reader
for line in sys.stdin:
	row = reader([line])
	entry = (list(row)[0])
	if(len(entry) != 22):
		print(entry[0]+"\t"+"Open")
	else:
		value = entry[14]+","+entry[6]+","+entry[2]+","+entry[1]
		print(entry[0]+"\t"+value)
