import csv
import psycopg2

# 连接到PostgreSQL数据库
conn = psycopg2.connect(
    host="localhost",
    database="postgres"
)
cur = conn.cursor()

# 读取CSV文件
with open('/Users/westernuniversity/Desktop/ECE9014/Project-part1/sql/Application/Application.Cities.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    for row in reader:
        # 创建INSERT语句
        cur.execute(
            "INSERT INTO Cities (DeliveryMethodID, DeliveryMethodName) VALUES (%s, %s)"
        )

# 提交事务并关闭连接
conn.commit()
cur.close()
conn.close()
