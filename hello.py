from pyspark.sql import SparkSession

# Create a spark session
# spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
spark = SparkSession.builder \
    .appName("KafkaReadTransformWriteToKafka") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Use sql() to write a raw SQL query
df = spark.sql("SELECT 'Hello World' as hello")

# Print the dataframe
df.show()
df.write.mode("overwrite").json("results")

# Apply transformation - converting lowercase messages to uppercase
transformed_df = df.withColumn("transformedMessage", upper(df.hello))

# Write the transformed messages to another Kafka topic
query = (
    transformed_df
    .selectExpr("CAST(transformedMessage AS STRING) AS value")
    .writeStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("topic", "dest-topic")
    .option("checkpointLocation", "checkpoint_folder")  # Specify the checkpoint location
    .start()
)

query.awaitTermination()
