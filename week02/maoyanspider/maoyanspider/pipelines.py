# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        # movie_list = []
        # movie_list.append(item['movie_name'])
        # movie_list.append(item['movie_type'])
        # movie_list.append(item['movie_date'])

        db = pymysql.connect("localhost", "test", "test123456", "maoyanspider")
        cursor = db.cursor()

        # 存在就删除并重新创建表
        cursor.execute("DROP TABLE IF EXISTS MOVIEINFO")
        sql = """CREATE TABLE MOVIEINFO (
            NAME CHAR(40),
            TYPE CHAR(20),
            DATE CHAR(20)
        )"""
        cursor.execute(sql)

        sql = """INSERT INTO MOVIEINFO(NAME, TYPE, DATE) VALUES (%s, %s, %s)
        """.format(item['movie_name'], item['movie_type'], item['movie_date'])

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        finally:
            db.close()
        # 插入数据
        return item
