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
	cols = df.map(lambda df: (df[2], float(df[12])))
	#print(cols.collect())

	violations = cols.combineByKey(lambda value: (value, 1),
                             lambda x, value: (x[0] + value, x[1] + 1),
                             lambda x, y: (x[0] + y[0], x[1] + y[1]))
	print(violations.collect())
	averageByKey = violations.map(lambda (label,value_sum,count)): (label, value_sum, value_sum / count))
	spark_result = averageByKey.map(lambda x: x[0] +'\t'+ str(x[1],x[2]))
	print("Before Printing")
	print(spark_result.collect())
	print("After Printing")
	#spark_result.saveAsTextFile("Spark/task3.out")
	#sc.stop() 