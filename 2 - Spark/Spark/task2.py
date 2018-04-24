import numpy as np
import sys
from operator import add
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: violation code")
		exit(-1)
	sc = SparkContext()
	# As a Text File
	files = sc.textFile(sys.argv[1], 1)
	# As a CSV file conversion
	df = files.mapPartitions(lambda x: reader(x))
	cols = df.map(lambda df: (df[2]))
	#print(cols.collect())
	violations = cols.map(lambda x: (x,1)).reduceByKey(add)
	spark_result = violations.map(lambda x: x[0] +'\t'+ str(x[1]))
	#print("Before Printing")
	#print(spark_result.collect())
	#print("After Printing")
	spark_result.saveAsTextFile("task2.out")
	sc.stop() 