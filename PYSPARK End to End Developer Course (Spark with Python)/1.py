from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize([("A", 1), ("B", 1), ("A", 5), ("B", 3)])
grouped = rdd.groupByKey()
result = grouped.mapValues(list).collect()

print(result)
