# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#from itemadapter import ItemAdapter
#import pandas as pd
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'root123',
    'charset' : 'utf8mb4',
    'db' : 'test1'
}
class SpidersPipeline:

    '''
    def process_item(self, item, spider):
        movie_list = []
        movie_list.append((item['title'], item['info'], item['post_time']))
        movies = pd.DataFrame(data=movie_list)
        movies.to_csv('./movies2.csv', encoding='utf8', mode='a', index=False, header=False)
        return item
    '''

    def __init__(self):
        # Connect to the database
        conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db'],
            charset=dbInfo['charset'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.conn = conn

    def open_spider(self, spider):
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        
        movie_name = item['title']
        movie_type = item['info']
        play_date = item['post_time']
# create table movie_info(movie_name varchar(50),movie_type varchar(50),play_date datetime);
        try:
            # Create a new record
            sql = "INSERT INTO `movie_info` (`movie_name`, `movie_type`, `play_date`) VALUES (%s, %s, %s)"
            values = (movie_name, movie_type, play_date)
            self.cur.execute(sql, values)
        except:
            self.cur.rollback()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.commit()
        self.conn.close()