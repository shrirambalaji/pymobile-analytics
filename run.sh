#!/bin/bash  
spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0,org.mongodb.mongo-hadoop:mongo-hadoop-core:1.3.1,org.mongodb:mongo-java-driver:3.4.2,org.mongodb.mongo-hadoop:mongo-hadoop-core:2.0.2,org.mongodb.mongo-hadoop:mongo-hadoop-spark:2.0.2  --py-files pymongo_spark.py,pymongo.egg  sentimentAnalysis.py
