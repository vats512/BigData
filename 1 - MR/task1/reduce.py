#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys

# input comes from STDIN (stream data that goes to the program)
lastKey = None
lastVal = None
keycount =0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    currentKey = key
    if(currentKey!=lastKey and lastKey!=None):
        if keycount == 1:
            if lastVal != 'Open':
                print('{0} {1}'.format(lastKey,lastVal))
        lastKey = currentKey
        lastVal = value
        keycount =1
    else:
        lastKey = currentKey
        lastVal = value
        keycount+=1

if (currentKey!=lastKey and keycount==1 and lastVal!='Open'):
    print('{0} {1}'.format(lastKey,lastVal))
