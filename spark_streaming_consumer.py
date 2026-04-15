from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, LongType

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", FloatType()),
    StructField("humidity", FloatType()),
    StructField("timestamp", LongType())
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .load()

parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

result = parsed.groupBy("sensor_id").avg("temperature", "humidity")

query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()