import traceback
import os
import sys

from pymysql import DatabaseError,connect

import dbinfo

print("当前的工作目录：" + os.getcwd())
print("python搜索模块的路径集合：", sys.path)
# 创建表
# mysql> CREATE TABLE movie2
#     -> (
#     -> id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     -> shorts VARCHAR(500),
#     -> stars INT(4),
#     -> );

class DBOperation(object):
    @classmethod
    def run(cls, sql):
        conn = connect( host=dbinfo.HOST,
                        port=dbinfo.PORT,
                        user=dbinfo.USERNAME,
                        password=dbinfo.PASSWORD,
                        db=dbinfo.DB)
        cur = conn.cursor()
        try:
            cur.execute(sql)
            cur.close()
            conn.commit()
            print("insert db !")
        except DatabaseError as e:
            print(e)
            conn.rollback()
        conn.close()

if __name__ == "__main__":
    stars_map = {
        "力荐": 5,
        "推荐": 4,
        "还行": 3,
        "较差": 2,
        "很差": 1
    }
    db = DBOperation()
    shorts = '这个电影好看'
    stars = stars_map["还行"]
    sql = f"""INSERT INTO movie2(shorts, stars) VALUES ('{shorts}', '{stars}');"""
    db.run(sql)