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
	cols = df.map(lambda df: (df[16]))
	
	#rows with NY
	ny_rows = cols.filter(lambda x: x == 'NY').map(lambda x: (x,1)).reduceByKey(add)
	#print("ny_rows_filter records are: ",ny_rows.collect())
	
	
	#rows without NY
	ny_wo_rows = cols.filter(lambda x: x != 'NY').map(lambda x: 'Other').map(lambda x: (x,1)).reduceByKey(add)
	#print("ny_wo_rows_filter records are: ",ny_wo_rows.collect())

	
	result = ny_rows.union(ny_wo_rows)
	#print("Result At last: ",result.collect(),"\n")
	
	spark_result = result.map(lambda x: x[0] +'\t'+ str(x[1]))
	#print("Before Printing")
	#print(spark_result.collect())
	#print("After Printing")
	spark_result.saveAsTextFile("task4.out")
	sc.stop() 