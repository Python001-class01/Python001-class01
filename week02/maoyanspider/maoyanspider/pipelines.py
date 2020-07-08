# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import traceback
from maoyanspider.db_config import configs

class MaoyanspiderPipeline:
    def __init__(self, host, database, table, user, password):
        self.host = host
        self.database = database
        self.table = table
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=configs['host'],
            database=configs['database'],
            table=configs['table'],
            user=configs['user'],
            password=configs['password']
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database)
        
    def process_item(self, item, spider):
        # movie_list = []
        # movie_list.append(item['movie_name'])
        # movie_list.append(item['movie_type'])
        # movie_list.append(item['movie_date'])
        
        cursor = self.db.cursor()

        # cursor.execute("DROP TABLE IF EXISTS MOVIEINFO")
        sql = """CREATE TABLE IF NOT EXISTS %s (
            NAME CHAR(40),
            TYPE CHAR(20),
            DATE CHAR(20)
        )""" % (self.table)
        cursor.execute(sql)

        sql = """INSERT INTO MOVIEINFO (NAME, TYPE, DATE) VALUES ("%s", "%s", "%s")""" % (item['movie_name'], item['movie_type'], item['movie_date'])

        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            traceback.print_exc()
            self.db.rollback()
        # 插入数据
        return item

    def close_spider(self, spider):
        self.db.close()
