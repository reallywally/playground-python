from pyspark.sql import SparkSession
import os

hadoop_host = "172.16.10.31"
hadoop_port = "10000"
hive_host = "172.16.10.31"
hive_port = "9083"

# SparkSession 생
spark = (SparkSession.builder
         .appName("Remote Hadoop/Hive Connection")
         .config("spark.hadoop.fs.defaultFS", f"hdfs://{hadoop_host}:{hadoop_port}")  # HDFS 설정
         .config("hive.metastore.uris", f"thrift://{hive_host}:{hive_port}")  # 하이브 메타스토어 연결
         .enableHiveSupport()  # 하이브 지원 활성화
         .getOrCreate())

# 데이터 조회
query = "SELECT * FROM feature_mart.fu_cust_inf WHERE cs_gem_cd = '01' LIMIT 5"
df = spark.sql(query)

# 결과를 딕셔너리 리스트로 변환
result_dict_list = [row.asDict() for row in df.collect()]

# 결과 출력
for row in result_dict_list:
    print(row)

# 세션 종료
spark.stop()