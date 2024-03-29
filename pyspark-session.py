#import findspark
#findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
#DataFrame Creation
# Lists, Tuples, Dictionaries, pyspark.sql.Rows, pandas DataFrame, RDD of such a list.
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row


df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df

#df.show()
#df.printSchema()

df = spark.createDataFrame([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')
df

#df.show()
#df.printSchema()

pandas_df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [2., 3., 4.],
    'c': ['string1', 'string2', 'string3'],
    'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
    'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
})
df = spark.createDataFrame(pandas_df)
df

#df.show()
#df.printSchema()

rdd = spark.sparkContext.parallelize([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
])
df = spark.createDataFrame(rdd, schema=['a', 'b', 'c', 'd', 'e'])
df

#df.show()
#df.printSchema()

#spark.conf.set('spark.sql.repl.eagerEval.enabled', True)
#df

df.show()
df.printSchema()

df.show(1)
df.show(1, vertical=True)
df.columns

#cool summary.
#count mean stddev min max
df.select("a", "b", "c").describe().show()

#Thrown out of memory when too large driver side
#collects from executors to driver side
#collects distributed data to the driver side as the local data
df.collect()
#In order to avoid throwing an out-of-memory exception, use DataFrame.take() or DataFrame.tail().
df.take(1)
df.tail(1)

df.toPandas()
df.a