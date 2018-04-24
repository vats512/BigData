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
	cols = df.map(lambda df: (df[2],df[1]) ).sortByKey()
	collection = cols.groupByKey().map(lambda df: (df[0], list(df[1])))
	print(collection.take(5))
	
	
	"""
	spark_result = answers.map(lambda x: x[0][0]+','+x[0][1] +'\t'+ str(x[1]))
	print(spark_result.collect())

	#print("Before Printing")
	print("\n",spark_result)
	#print("After Printing")
	
	#spark_result.saveAsTextFile("Spark/task5.out")
	sc.stop() 

	"""