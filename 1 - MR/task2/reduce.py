#!/usr/bin/env python

import sys
import string

key = None
currentkey = None
count = 0
for line in sys.stdin:

        line = line.strip()
        key,value = line.split("\t",1)

        if key == currentkey:
                count = count+1
        else:
                if currentkey == None: #First time
                        count = 1
                else:
                        print(str(currentkey)+"\t"+str(count))
                        count = 1                
                currentkey = key
#for the last key
print(str(key)+"\t"+str(count))

