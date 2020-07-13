import pymysql
import pandas as pd

'''
内容较多，把做题过程中，搜索的网页，老师的代码，全部吸收进来了；
老师批阅时，忽略注释；
union 去掉重复的，没有搞定，？？？？？？？？？？？？？
一边写，一边cmd 里面操作mysql ，对比结果，写在文档最后面
'''

#1. SELECT * FROM data;   实现代码如下：

sql  =  'SELECT * FROM ttt'
#conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root123',port=3306,db='test1',charset='utf8')
df = pd.read_sql(sql,conn)
print(df)
print("------")
#2. SELECT * FROM data LIMIT(10);
print(df[1:11])


#3. SELECT id FROM data;

print(df["id"])
print("---------------------")
#4. SELECT COUNT(id) FROM data;
print(df["id"].count())

print("---------------------")
#5. SELECT * FROM ttt WHERE id<1000 AND salary>3000;
# 过滤数据
#df['star'] == '力荐'
#df [ df['star'] == '力荐' ]
#and df["salary"]>3000]

print(df[ (df["id"]<10) & (df["salary"]>3000 ) ])
print("5555555555555555555555")


#6. SELECT id,COUNT(DISTINCT order_id) FROM ttt GROUP BY id;

# 我不会 ，我查到这个网页 pandas distinct groupby 
# https://stackoverflow.com/questions/15411158/pandas-countdistinct-equivalent
t=df.groupby('id').order_id.nunique()
print(t)

print("---------------")




#7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;

#7. SELECT * FROM ttt t1 INNER JOIN tt2 t2 ON t1.id = t2.id;



'''

pd.merge(df1, df2, on='id')
CREATE TEMPORARY TABLE tt2 AS (SELECT *  FROM ttt);
sql  =  'SELECT * FROM ttt'
#conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root123',port=3306,db='test1',charset='utf8')
df = pd.read_sql(sql,conn)

CREATE TABLE tt2 (id int,name varchar(10),salary int ,order_id int);

'''
sql2  =  'SELECT * FROM tt2'
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root123',port=3306,db='test1',charset='utf8')
df = pd.read_sql(sql,conn)
df2= pd.read_sql(sql2,conn)
print(pd.merge(df, df2, on='id'))
print("77777777777777777777777777777777777777")



#8. SELECT * FROM table1 UNION SELECT * FROM table2;
union2 = pd.concat([df, df2], ignore_index=True)
print(union2)
'''
如何实现去掉重复的？----这是一个我自己没有解决的问题；？？？？？？
import pandas as pd

clients1 = {'clientFirstName': ['Jon','Maria','Bruce','Lili'],
            'clientLastName': ['Smith','Lam','Jones','Chang'],
            'country': ['US','Canada','Italy','China']
           }

df1 = pd.DataFrame(clients1, columns= ['clientFirstName', 'clientLastName','country'])


clients2 = {'clientFirstName': ['Bill','Jack','Elizabeth','Jenny'],
            'clientLastName': ['Jackson','Green','Gross','Sing'],
            'country': ['UK','Germany','Brazil','Japan']
           }

df2 = pd.DataFrame(clients2, columns= ['clientFirstName', 'clientLastName','country'])

union = pd.concat([df1, df2], ignore_index=True)
print (union)
'''



#9. DELETE FROM table1 WHERE id=10;
#9. DELETE FROM ttt WHERE id=10;
print(df[ (df["id"] != 10)])
print(99999999999)
 
#10. ALTER TABLE table1 DROP COLUMN column_name;
#10. ALTER TABLE ttt DROP COLUMN column_name;
#不要哪一列，直接不选就可以了；不要去删数据库的真实表；这里order_id 这一列没有选中
print(df["id","name","salary"])

'''


111111111111
from sklearn import datasets #引入数据集
# 鸢尾花数据集
iris = datasets.load_iris()
X, y = iris.data, iris.target

# 查看特征
iris.feature_names

# 查看标签
iris.target_names

# 按照3比1的比例划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)


# load_xxx 各种数据集
# load_boston Boston房屋价格 回归
# load_digits 手写体  分类
# load_iris   鸢尾花 分类聚类
===================
22222222222222222222222222
import pandas as pd
import numpy as np
import matplotlib as plt
import os
pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd,'book_utf8.csv')
# df = pd.read_csv('book_utf8.csv')
df = pd.read_csv(book)
# 输出全部内容
print(df)

# 筛选标题为"还行"这一列
df['还行']

# 切片方式筛选
# 显示前3行
df[1:3]

# 增加列名
df.columns = ['star', 'vote', 'shorts']

# 显示特定的行、列
df.loc[1:3, ['star']]

# 过滤数据
df['star'] == '力荐'
df [ df['star'] == '力荐' ]

# 缺失数据
df.dropna()

# 数据聚合
df.groupby('star').sum()

# 创建新列
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)

print(df)
==================================
33333333333
import pandas as pd
import numpy as np

# 从列表创建Series
pd.Series(['a', 'b', 'c'])
# 0    a
# 1    b
# 2    c
# dtype: object
# 自动创建索引

# 通过字典创建带索引的Series
s1 = pd.Series({'a':11, 'b':22, 'c':33})
# 通过关键字创建带索引的Series
s2 = pd.Series([11, 22, 33], index = ['a', 'b', 'c'])
s1
s2

# 获取全部索引
s1.index
# 获取全部值
s1.values

# 类型
type(s1.values)    # <class 'numpy.ndarray'>
type(np.array(['a', 'b']))

# 转换为列表
s1.values.tolist()

# 使用index会提升查询性能
#    如果index唯一，pandas会使用哈希表优化，查询性能为O(1)
#    如果index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)
#    如果index完全随机，每次查询都要扫全表，查询性能为O(N)

# 取出email
emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
import re
pattern ='[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
emails[mask]
UPDATE categories
    SET order_id = CASE id
        WHEN 1 THEN 3
        WHEN 2 THEN 4
        WHEN 3 THEN 5
    END,
    title = CASE id
        WHEN 1 THEN 'New Title 1'
        WHEN 2 THEN 'New Title 2'
        WHEN 3 THEN 'New Title 3'
    END
ALTER TABLE ttt ADD order_id int(10);

#CREATE TABLE ttt(id INT(11),name VARCHAR(25),salary FLOAT);

INSERT INTO ttt VALUES (1,"test1",1000),(2,"test2",2000),(3,"test3",3000),(4,"test4",4000);

44444444444444444
import pandas as pd


# 列表创建dataframe
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
# 嵌套列表创建dataframe
df2 = pd.DataFrame([
                     ['a', 'b'], 
                     ['c', 'd']
                    ])
# 自定义列索引
df2.columns= ['one', 'two']
# 自定义行索引
df2.index = ['first', 'second']

df2
# 可以在创建时直接指定 DataFrame([...] , columns='...', index='...' )
# 查看索引
df2.columns, df2.index
type(df2.values)
------------------------



555555555555555
import pandas as pd
# pip install xlrd
# 导入excel文件
excel1 = pd.read_excel(r'1.xlsx')
excel1
# 指定导入哪个Sheet
pd.read_excel(r'1.xlsx',sheet_name = 0)

# 支持其他常见类型
pd.read_csv(r'c:\file.csv',sep=' ', nrows=10, encoding='utf-8')

pd.read_table( r'file.txt' , sep = ' ')

import pymysql
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)


# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape

# 详细信息
excel1.info()
excel1.describe()
=====================================
Microsoft Windows [版本 10.0.18362.53]
(c) 2019 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>f:

F:\>cd F:\mysql-8.0.20-winx64

F:\mysql-8.0.20-winx64>cd bin

F:\mysql-8.0.20-winx64\bin>mysqld --initialize --console
2020-07-12T09:06:09.041128Z 0 [System] [MY-013169] [Server] F:\mysql-8.0.20-winx64\bin\mysqld.exe (mysqld 8.0.20) initializing of server in progress as process 4936
2020-07-12T09:06:09.054937Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2020-07-12T09:06:15.928936Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2020-07-12T09:06:35.677976Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: up..GDski1:U

F:\mysql-8.0.20-winx64\bin>net start mysql
服务名无效。

请键入 NET HELPMSG 2185 以获得更多的帮助。


F:\mysql-8.0.20-winx64\bin>mysqld --install MySQL3306 --defaults-file=F:\mysql-8.0.20-winx64\mysql.ini
Service successfully installed.

F:\mysql-8.0.20-winx64\bin>net start mysql
服务名无效。

请键入 NET HELPMSG 2185 以获得更多的帮助。


F:\mysql-8.0.20-winx64\bin>net start mysql3306
MySQL3306 服务正在启动 ...
MySQL3306 服务已经启动成功。


F:\mysql-8.0.20-winx64\bin>mysql -h localhost -P 3308 -u root -p
Enter password: **
ERROR 2003 (HY000): Can't connect to MySQL server on 'localhost' (10061)

F:\mysql-8.0.20-winx64\bin>mysql -h localhost -P 3306 -u root -p
Enter password: ************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.20

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root123';
Query OK, 0 rows affected (0.40 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.13 sec)

mysql> CREATE USER 'root'@'%' IDENTIFIED BY 'root123';
Query OK, 0 rows affected (0.37 sec)

mysql> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root123';
Query OK, 0 rows affected (0.38 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.16 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.16 sec)

mysql> show databases;
ERROR 2013 (HY000): Lost connection to MySQL server during query
mysql> exit
Bye

F:\mysql-8.0.20-winx64\bin>mysql -h localhost -P 3306 -u root -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.20 MySQL Community Server - GPL

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.19 sec)

mysql> create database test1;
Query OK, 1 row affected (0.39 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test1              |
+--------------------+
5 rows in set (0.00 sec)

mysql> use test1;
Database changed
mysql> show tables;
Empty set (0.34 sec)

mysql> CREATE TABLE ttt(id INT(11),name VARCHAR(25),salary FLOAT);
Query OK, 0 rows affected, 1 warning (0.66 sec)

mysql> show tables;
+-----------------+
| Tables_in_test1 |
+-----------------+
| ttt             |
+-----------------+
1 row in set (0.11 sec)

mysql> select * from ttt;
Empty set (0.01 sec)

mysql> INSERT INTO ttt VALUES (1,"test1",1000),(2,"test2",2000),(3,"test3",3000),(4,"test4",4000);
Query OK, 4 rows affected (0.47 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from ttt;
+------+-------+--------+
| id   | name  | salary |
+------+-------+--------+
|    1 | test1 |   1000 |
|    2 | test2 |   2000 |
|    3 | test3 |   3000 |
|    4 | test4 |   4000 |
+------+-------+--------+
4 rows in set (0.00 sec)

mysql> INSERT INTO ttt VALUES (5,"test5",5000),(6,"test6",6000),(7,"test7",7000),(8,"test8",8000);
Query OK, 4 rows affected (0.37 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> INSERT INTO ttt VALUES (9,"test9",9000),(10,"test10",10000),(11,"test11",11000),(12,"test12",12000);
Query OK, 4 rows affected (0.37 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from ttt;
+------+--------+--------+
| id   | name   | salary |
+------+--------+--------+
|    1 | test1  |   1000 |
|    2 | test2  |   2000 |
|    3 | test3  |   3000 |
|    4 | test4  |   4000 |
|    5 | test5  |   5000 |
|    6 | test6  |   6000 |
|    7 | test7  |   7000 |
|    8 | test8  |   8000 |
|    9 | test9  |   9000 |
|   10 | test10 |  10000 |
|   11 | test11 |  11000 |
|   12 | test12 |  12000 |
+------+--------+--------+
12 rows in set (0.00 sec)

mysql> INSERT INTO ttt VALUES (12,"te3333st12",1442000);
Query OK, 1 row affected (0.35 sec)

mysql> SELECT COUNT(id) FROM ttt;
+-----------+
| COUNT(id) |
+-----------+
|        13 |
+-----------+
1 row in set (0.34 sec)

mysql> ALTER TABLE ttt ADD order_id int(10);
Query OK, 0 rows affected, 1 warning (0.64 sec)
Records: 0  Duplicates: 0  Warnings: 1

mysql> select * from ttt;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |     NULL |
|    2 | test2      |    2000 |     NULL |
|    3 | test3      |    3000 |     NULL |
|    4 | test4      |    4000 |     NULL |
|    5 | test5      |    5000 |     NULL |
|    6 | test6      |    6000 |     NULL |
|    7 | test7      |    7000 |     NULL |
|    8 | test8      |    8000 |     NULL |
|    9 | test9      |    9000 |     NULL |
|   10 | test10     |   10000 |     NULL |
|   11 | test11     |   11000 |     NULL |
|   12 | test12     |   12000 |     NULL |
|   12 | te3333st12 | 1442000 |     NULL |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update ttt set order_id=9;
Query OK, 13 rows affected (0.36 sec)
Rows matched: 13  Changed: 13  Warnings: 0

mysql> select * from ttt;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |        9 |
|    2 | test2      |    2000 |        9 |
|    3 | test3      |    3000 |        9 |
|    4 | test4      |    4000 |        9 |
|    5 | test5      |    5000 |        9 |
|    6 | test6      |    6000 |        9 |
|    7 | test7      |    7000 |        9 |
|    8 | test8      |    8000 |        9 |
|    9 | test9      |    9000 |        9 |
|   10 | test10     |   10000 |        9 |
|   11 | test11     |   11000 |        9 |
|   12 | test12     |   12000 |        9 |
|   12 | te3333st12 | 1442000 |        9 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update ttt set order_id=orerder_id +id ;
ERROR 1054 (42S22): Unknown column 'orerder_id' in 'field list'
mysql> update ttt set order_id=id+77 ;
Query OK, 13 rows affected (0.38 sec)
Rows matched: 13  Changed: 13  Warnings: 0

mysql> select * from ttt;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       80 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |       89 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update ttt set order_id=id+789 where salary>20000 ;
Query OK, 1 row affected (0.39 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from ttt;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       80 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update ttt set order_id=79 where id =3 ;
Query OK, 1 row affected (0.36 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT id,COUNT(DISTINCT order_id) FROM ttt GROUP BY id;
+------+--------------------------+
| id   | COUNT(DISTINCT order_id) |
+------+--------------------------+
|    1 |                        1 |
|    2 |                        1 |
|    3 |                        1 |
|    4 |                        1 |
|    5 |                        1 |
|    6 |                        1 |
|    7 |                        1 |
|    8 |                        1 |
|    9 |                        1 |
|   10 |                        1 |
|   11 |                        1 |
|   12 |                        2 |
+------+--------------------------+
12 rows in set (0.35 sec)

mysql> SELECT id,COUNT(DISTINCT order_id) FROM ttt GROUP BY id;
+------+--------------------------+
| id   | COUNT(DISTINCT order_id) |
+------+--------------------------+
|    1 |                        1 |
|    2 |                        1 |
|    3 |                        1 |
|    4 |                        1 |
|    5 |                        1 |
|    6 |                        1 |
|    7 |                        1 |
|    8 |                        1 |
|    9 |                        1 |
|   10 |                        1 |
|   11 |                        1 |
|   12 |                        2 |
+------+--------------------------+
12 rows in set (0.00 sec)

mysql> select * into ttt2 from ttt;
ERROR 1327 (42000): Undeclared variable: ttt2
mysql> select * into #ttt2 from ttt;
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> select * from ttt;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       79 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> CREATE TEMPORARY TABLE tt2 AS (SELECT *  FROM ttt);
Query OK, 13 rows affected (0.01 sec)
Records: 13  Duplicates: 0  Warnings: 0

mysql> select tt2
    -> ;
ERROR 1054 (42S22): Unknown column 'tt2' in 'field list'
mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       79 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       79 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> drop table tt2;
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE tt2 (id int,name varchar(10),salary int ,order_id int);
Query OK, 0 rows affected (0.29 sec)

mysql> select * from tt2;
Empty set (0.00 sec)

mysql> insert into tt2 select * from ttt;
Query OK, 13 rows affected (0.37 sec)
Records: 13  Duplicates: 0  Warnings: 0

mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       79 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update tt2 set salary = salary +7 ;
Query OK, 13 rows affected (0.38 sec)
Rows matched: 13  Changed: 13  Warnings: 0

mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1007 |       78 |
|    2 | test2      |    2007 |       79 |
|    3 | test3      |    3007 |       79 |
|    4 | test4      |    4007 |       81 |
|    5 | test5      |    5007 |       82 |
|    6 | test6      |    6007 |       83 |
|    7 | test7      |    7007 |       84 |
|    8 | test8      |    8007 |       85 |
|    9 | test9      |    9007 |       86 |
|   10 | test10     |   10007 |       87 |
|   11 | test11     |   11007 |       88 |
|   12 | test12     |   12007 |       89 |
|   12 | te3333st12 | 1442007 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update tt2 set id = id +7 ;
Query OK, 13 rows affected (0.37 sec)
Rows matched: 13  Changed: 13  Warnings: 0

mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    8 | test1      |    1007 |       78 |
|    9 | test2      |    2007 |       79 |
|   10 | test3      |    3007 |       79 |
|   11 | test4      |    4007 |       81 |
|   12 | test5      |    5007 |       82 |
|   13 | test6      |    6007 |       83 |
|   14 | test7      |    7007 |       84 |
|   15 | test8      |    8007 |       85 |
|   16 | test9      |    9007 |       86 |
|   17 | test10     |   10007 |       87 |
|   18 | test11     |   11007 |       88 |
|   19 | test12     |   12007 |       89 |
|   19 | te3333st12 | 1442007 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> SELECT * FROM ttt t1 INNER_JOIN tt2 t2 ON t1.id = t2.id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'INNER_JOIN tt2 t2 ON t1.id = t2.id' at line 1
mysql> SELECT * FROM ttt t1 INNER JOIN tt2 t2 ON t1.id = t2.id;
+------+------------+---------+----------+------+-------+--------+----------+
| id   | name       | salary  | order_id | id   | name  | salary | order_id |
+------+------------+---------+----------+------+-------+--------+----------+
|    8 | test8      |    8000 |       85 |    8 | test1 |   1007 |       78 |
|    9 | test9      |    9000 |       86 |    9 | test2 |   2007 |       79 |
|   10 | test10     |   10000 |       87 |   10 | test3 |   3007 |       79 |
|   11 | test11     |   11000 |       88 |   11 | test4 |   4007 |       81 |
|   12 | test12     |   12000 |       89 |   12 | test5 |   5007 |       82 |
|   12 | te3333st12 | 1442000 |      801 |   12 | test5 |   5007 |       82 |
+------+------------+---------+----------+------+-------+--------+----------+
6 rows in set (0.00 sec)

mysql> select * from ttt;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       79 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    8 | test1      |    1007 |       78 |
|    9 | test2      |    2007 |       79 |
|   10 | test3      |    3007 |       79 |
|   11 | test4      |    4007 |       81 |
|   12 | test5      |    5007 |       82 |
|   13 | test6      |    6007 |       83 |
|   14 | test7      |    7007 |       84 |
|   15 | test8      |    8007 |       85 |
|   16 | test9      |    9007 |       86 |
|   17 | test10     |   10007 |       87 |
|   18 | test11     |   11007 |       88 |
|   19 | test12     |   12007 |       89 |
|   19 | te3333st12 | 1442007 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> update tt2 set id=12,salary=1442000 where order_id=801
    -> ;
Query OK, 1 row affected (0.40 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    8 | test1      |    1007 |       78 |
|    9 | test2      |    2007 |       79 |
|   10 | test3      |    3007 |       79 |
|   11 | test4      |    4007 |       81 |
|   12 | test5      |    5007 |       82 |
|   13 | test6      |    6007 |       83 |
|   14 | test7      |    7007 |       84 |
|   15 | test8      |    8007 |       85 |
|   16 | test9      |    9007 |       86 |
|   17 | test10     |   10007 |       87 |
|   18 | test11     |   11007 |       88 |
|   19 | test12     |   12007 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
+------+------------+---------+----------+
13 rows in set (0.00 sec)

mysql> select * from ttt union select * from tt2;
+------+------------+---------+----------+
| id   | name       | salary  | order_id |
+------+------------+---------+----------+
|    1 | test1      |    1000 |       78 |
|    2 | test2      |    2000 |       79 |
|    3 | test3      |    3000 |       79 |
|    4 | test4      |    4000 |       81 |
|    5 | test5      |    5000 |       82 |
|    6 | test6      |    6000 |       83 |
|    7 | test7      |    7000 |       84 |
|    8 | test8      |    8000 |       85 |
|    9 | test9      |    9000 |       86 |
|   10 | test10     |   10000 |       87 |
|   11 | test11     |   11000 |       88 |
|   12 | test12     |   12000 |       89 |
|   12 | te3333st12 | 1442000 |      801 |
|    8 | test1      |    1007 |       78 |
|    9 | test2      |    2007 |       79 |
|   10 | test3      |    3007 |       79 |
|   11 | test4      |    4007 |       81 |
|   12 | test5      |    5007 |       82 |
|   13 | test6      |    6007 |       83 |
|   14 | test7      |    7007 |       84 |
|   15 | test8      |    8007 |       85 |
|   16 | test9      |    9007 |       86 |
|   17 | test10     |   10007 |       87 |
|   18 | test11     |   11007 |       88 |
|   19 | test12     |   12007 |       89 |
+------+------------+---------+----------+
25 rows in set (0.01 sec)

mysql>
'''