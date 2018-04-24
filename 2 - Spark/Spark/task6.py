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
	cols = df.map(lambda df: (df[14],df[16]))
	#print(cols.collect())
	

	violations = cols.map(lambda x: (x,1)).reduceByKey(add).takeOrdered(20, key=lambda x: (-x[1],x[0]))
	#print(violations[:][0][0])
	
	answers = sc.parallelize(violations)
	#print(answers.collect())
	#spark_result = str(violations[:][0][0]) +"\t"+ str(violations[:][0][1])
	spark_result = answers.map(lambda x: x[0][0]+','+x[0][1] +'\t'+ str(x[1]))
	#print(spark_result.collect())

	#print("Before Printing")
	print("\n",spark_result)
	#print("After Printing")
	
	spark_result.saveAsTextFile("task6.out")
	sc.stop() 