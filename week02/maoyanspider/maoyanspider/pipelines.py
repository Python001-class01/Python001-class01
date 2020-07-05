# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import traceback
from maoyanspider.db_config import configs

class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        # movie_list = []
        # movie_list.append(item['movie_name'])
        # movie_list.append(item['movie_type'])
        # movie_list.append(item['movie_date'])
        
        db = pymysql.connect(configs['host'], configs['user'], configs['password'], "maoyanspider")
        cursor = db.cursor()

        # cursor.execute("DROP TABLE IF EXISTS MOVIEINFO")
        sql = """CREATE TABLE IF NOT EXISTS MOVIEINFO (
            NAME CHAR(40),
            TYPE CHAR(20),
            DATE CHAR(20)
        )"""
        cursor.execute(sql)

        sql = """INSERT INTO MOVIEINFO (NAME, TYPE, DATE) VALUES ("%s", "%s", "%s")""" % (item['movie_name'], item['movie_type'], item['movie_date'])

        try:
            cursor.execute(sql)
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
        finally:
            db.close()
        # 插入数据
        return item
