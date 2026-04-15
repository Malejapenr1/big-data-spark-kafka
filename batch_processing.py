from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BatchProcessing").getOrCreate()

data = [
    (1, "A", 23),
    (2, "B", 45),
    (3, "A", 30),
    (4, "B", 50)
]

columns = ["id", "category", "value"]

df = spark.createDataFrame(data, columns)

df.show()

df.groupBy("category").avg("value").show()