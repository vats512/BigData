#!/usr/bin/env python

import sys
import string

key = None
currentkey = None
total = 0
count = 0
for line in sys.stdin:
        line = line.strip()
        key,value = line.split("\t",1)
        #If error then convert key to str(key)
        if key == currentkey:
                total = total + float(value)
                count = count+1
        else:
                if currentkey == None: #First time
                        total = float(value)
                        count = 1
                else:
                        avg = float(total/count)
                        print("{0:s}\t{1:.2f}, {2:.2f}".format(currentkey,total,avg))
                        total = float(value)
                        count = 1
                        avg = 0                
        currentkey = key
#for the last key
avg = float(total/count)
print("{0:s}\t{1:.2f}, {2:.2f}".format(currentkey,total,avg))

