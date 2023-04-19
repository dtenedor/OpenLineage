# Copyright 2018-2023 contributors to the OpenLineage project
# SPDX-License-Identifier: Apache-2.0

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .config("parentProject", "openlineage-ci") \
    .config("credentialsFile", "/opt/gcloud/gcloud-service-key.json") \
    .config("temporaryGcsBucket", "openlineage-spark-bigquery-integration") \
    .appName("OpenLineage Spark Bigquery") \
    .getOrCreate()


PROJECT_ID = 'openlineage-ci'
DATASET_ID = 'airflow_integration'

version_name = str(spark.version).replace(".", "_")

source_table = f"{PROJECT_ID}.{DATASET_ID}.{version_name}_source"
target_table = f"{PROJECT_ID}.{DATASET_ID}.{version_name}_target"

spark.sparkContext.setLogLevel('info')


g

first = spark.read.format('bigquery') \
    .option('table', source_table) \
    .load()

first.write.format('bigquery') \
    .option('table', target_table) \
    .mode('overwrite') \
    .save()
