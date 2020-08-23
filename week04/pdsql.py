import pandas as pd
import pymysql

conn = pymysql.connect('ip', 'name', 'pass', 'dbname', charset=utf8)
sql1 = 'select * from data'
# select * from data
s1 = pd.read_sql(sql1, conn)

# select * from data limit 10
s2 = s1.head(10)

# select id from data
s3 = s1['id']

#select count(id) from data
s4 = s1['id'].count()

# select * from data where id < 1000 and age > 30
s5 = s1[(s1['id'] < 1000) & (s1['age'] > 30)]


sql2 = 'select * from table1'
t1 = pd.read_sql(sql2,conn)
# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# 这个我还没弄明白，disinct count
s6 = t1.groupby('id').aggregate({'id':'count', 'order_id':'count'})

sql3 = 'select * from table2'
t2 = pd.read_sql(sql2,conn)

#SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id
s7 = pd.merge(t1, t2, on = 'id')

# SELECT * FROM table1 UNION SELECT * FROM table2
s8 = pd.merge(t1, t2, how = 'outer')

#DELETE FROM table1 WHERE id=10
ids = t1['id']
cols = [i for i in range(ids.size) if ids.iat[i] == 10]
s9 = t1.drop(cols)

#ALTER TABLE table1 DROP COLUMN column_name
s10 = t1.drop(['columns_name'])
