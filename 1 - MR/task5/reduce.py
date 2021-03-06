#!/usr/bin/env python

import sys
import string

key = None
currentkey = None
count = 0
mydict = {}
for line in sys.stdin:
        line = line.strip()
        key,value = line.split("\t",1)
        #If error then convert key to str(key)
        
        if key == currentkey:
                count = count+1
        else:
                if currentkey == None: #First time
                        count = 1
                else:
                        mydict[currentkey] = count
                        count = 1                
                currentkey = key
#for the last key
mydict[currentkey] = count
high_key, high_value = max(mydict.items(), key=lambda x:x[1])
print("{0:s}\t{1:d}".format(str(high_key),int(high_value)))
