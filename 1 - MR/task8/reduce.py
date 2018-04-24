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
                count += 1
        else:
                if currentkey == None:
                        count = 1
                else:
                        if 'a00' in currentkey:
                                print('{0}, {1}'.format(currentkey.replace('a00','vehicle_make\t'), count))
                        else:
                                print('{0}, {1}'.format(currentkey.replace('b11','vehicle_color\t'), count))
                count = 1
                currentkey = key
if 'a00' in currentkey:
        print('{0}, {1}'.format(currentkey.replace('a00','vehicle_make\t'), count))
else:
        print('{0}, {1}'.format(currentkey.replace('b11','vehicle_color\t'), count))



