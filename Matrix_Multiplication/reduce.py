#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string

#number of columns of A/rows of B
n = int(sys.argv[1]) 
#Create data structures to hold the current row/column values (if needed; your code goes here)
currentkey = None
key = None
matrix_elements = {}
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	#Remove leading and trailing whitespace
	line = line.strip()
	#Get key/value 
	key, value = line.split('\t',1)
	#Parse key/value input (your code goes here)
	values = value.split(" ")
	box = values[1]
	indexi = values[2]
	indexj = values[3]
	#If we are still on the same key...
	if key==currentkey:
		#Process key/value pair (your code goes here)
		if indexi not in matrix_elements:
			matrix_elements[indexi] = indexj
		else:
			wo_multiplied  = matrix_elements[indexi]
			multiplied = float(wo_multiplied) * float(indexj)
			matrix_elements[indexi] = multiplied
	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		#compute/output result to STDOUT (your code goes here)
		if currentkey == None:
			matrix_elemets = {}
			matrix_elements[indexi] = indexj	
		else:
			sum = 0.0
			for index in matrix_elements:
        			sum = sum + float( matrix_elements[index])
			print("{0:s}\t {1:f}".format(currentkey, sum))
			matrix_elements = {}
			matrix_elements[indexi] = indexj
		currentkey = key
		#Process input for new key (your code goes here)
#Compute/output result for the last key (your code goes here)
sum = 0.0
for indexi in matrix_elements:
	sum = sum + float( matrix_elements[indexi])
print("{0:s}\t {1:f}".format(currentkey, sum))



