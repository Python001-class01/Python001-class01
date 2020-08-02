# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from doubanspider.db_config import configs
import pymysql
import traceback


class DoubanspiderPipeline:
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
        self.db = pymysql.connect(
            self.host, self.user, self.password, self.database)

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = f"""CREATE TABLE IF NOT EXISTS {self.table} (
            CID INT,
            COMMENT VARCHAR(350),
            RATE INT
        )"""
        cursor.execute(sql)

        sql = f"""INSERT INTO {self.table} (CID, COMMENT, RATE) VALUES ("{item['cid']}", "{item['comment']}", "{item['rate']}")
        """
        try:
            cursor.execute(sql)
            self.db.commit()
            print("insert successsssss")
        except Exception:
            traceback.print_exc()
            self.db.rollback()
        return item

    def close_spider(self, spider):
        self.db.close()
