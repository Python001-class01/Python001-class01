# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class MoviesPipeline():
    def __init__(self, host, port, user, password, database, table):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    # 仿中间件获取setting里的数据库配置
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            table=crawler.settings.get('MYSQL_TABLE')
        )

    # 开启爬虫时执行连接数据库，只执行一次
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database,
            charset='utf8mb4',
        )
        # 游标建立的时候就开启了一个隐形的事务
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            # 变量尽可能的靠传值
            sql_fmt = ("""INSERT INTO `{}`(`title`, `type`, `time`) VALUES ('{}', '{}', '{}');""")
            sql = sql_fmt.format(self.table, item['title'], item['type'], item['time'])
            self.cursor.execute(sql)
            self.conn.commit()
            return item
        except  Exception as e:
            self.conn.rollback()
            self.logger.error(e)

    # 关闭爬虫时执行，只执行一次(注：如果爬虫中间发生异常导致崩溃，close_spider可能也不会执行)
    def close_spider(self, spider):
        self.conn.close()
