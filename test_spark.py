from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip


def get_spark_session():
    builder = SparkSession.builder.config(
        "spark.jars.packages", "io.delta:delta-core_2.12:1.0.0"
    )
    return configure_spark_with_delta_pip(builder).getOrCreate()


spark = get_spark_session()

df = spark.createDataFrame(data=[("Sushant", 23)], schema=["Name", "Age"])

example_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14]]

print(df.show())
