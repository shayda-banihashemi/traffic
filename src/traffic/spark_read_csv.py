# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def read_csv_with_spark():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("CSV Reader") \
        .master("local[*]") \
        .getOrCreate()

    try:
        # Path to your CSV file - replace with your actual file path
        csv_file_path = "/Users/shaydabanihashemi/data/lake/bronze/utd19_u.csv"

        metrics = spark.read.option("header", "true") \
            .option("inferSchema", "true") \
            .csv(csv_file_path)
        metrics = metrics.filter(metrics.error.isNull())
        metrics = metrics.filter(~metrics.speed.isNull())

        csv_file_path = "/Users/shaydabanihashemi/data/lake/bronze/detectors_public.csv"

        detectors = spark.read.option("header", "true") \
            .option("inferSchema", "true") \
            .csv(csv_file_path)

        #Join data tables
        df = metrics.join(detectors, 'detid')

        #df.write.parquet('/Users/shaydabanihashemi/data/lake/silver/traffic.parquet')

        # Display the inferred schema
        print("Schema of the DataFrame:")
        df.printSchema()

        # Show the first few rows of the data
        print("\nSample data:")
        df.show(30)

        # Perform some basic operations
        print("\nNumber of rows:", df.count())

        # Select specific columns
        print("\nSelecting specific columns:")
        df.select(df.columns[:2]).show(5)

        # Filter data
        print("\nFiltered data:")
        if "age" in df.columns:
            df.filter(col("age") > 25).show(5)

        # Group by and aggregate
        print("\nGrouped data:")
        if len(df.columns) > 1:
            df.groupBy(df.columns[0]).count().show(5)

        print("\nDistinct Values in City Code")
        df.select("citycode").distinct().show()

        #for city in df.select('citycode'):
        print("\nRecords for Birmigham")
        df.select("day", "flow", "speed","limit","citycode").where(df.citycode == "birmingham").show()

        print("\nDistinct Values in Road and City Code")
        df.select("road","citycode").distinct().show()

        return df

    finally:
        # Stop the Spark session
        spark.stop()
        print("Spark session stopped")

if __name__ == "__main__":
    print("Starting Spark CSV reader")
    df = read_csv_with_spark()
    print("Finished processing CSV file")