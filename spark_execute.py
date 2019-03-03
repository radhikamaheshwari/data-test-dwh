import spark
import pyspark
import os
import visualize_dag
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
from pyspark.sql import functions as F
from pyspark.sql.functions import udf, encode
from pyspark.sql.types import DoubleType, IntegerType, StringType

pwd = os.getcwd()
print pwd
conf = SparkConf() \
    .setAppName("Run SQl Parallelly as per DAG") \

sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

spark_dag=[]
for element in visualize_dag.stack:
    if not element.startswith('raw'):
        spark_dag.append(element)

# for element in spark_dag:
#     print element


def read_data(path):
    return sqlContext.read.csv(path)


def calling():
    # sqlContext.sql("create database if not exists raw")
    # sqlContext.sql("use raw")
    categories= read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_categories",mode="overwrite")
    inventory_items=read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_inventory_items", mode="overwrite")
    pictures = read_data(pwd+'/raw/pictures').write.saveAsTable("raw_pictures",mode="overwrite")
    product_groups = read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_product_groups",mode="overwrite")
    products = read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_products",mode="overwrite")
    purchase_items = read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_purchase_items",mode="overwrite")
    purchase_line_items = read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_purchase_line_items",mode="overwrite")
    purchases = read_data(pwd+'/raw/inventory_items').write.saveAsTable("raw_purchases",mode="overwrite")

    # sqlContext.sql("create database if not exists tmp")
    # sqlContext.sql("use tmp")
    for element in spark_dag:
        element=element.replace('tmp_','tmp/')+'.sql'
        print (element)
        with open(os.getcwd() + '/'+element) as sqlfile:
            dfsql=sqlfile.read()
            sqlContext.sql(dfsql);
        #sqlContext.sql(os.getcwd() + '/' + element).toDF().saveAsTable(element, mode="overwrite")


calling();

#if __name__ == '__main__':
#    main()