# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import os

class MaoyanPipeline:
    def __init__(self):
        # csv文件的位置，无需事先实现
        store_file = os.path.dirname(__file__) + '/spiders/rankList.csv'
        print('**************')

        # 打开创建文件
        self.file = open(store_file, 'a+', encoding='utf8', newline='')
        # csv写法
        self.writer = csv.writer(self.file, dialect='excel')

    def process_item(self, item, spider):
        # 判断字段值不为空再写入文件
        print('正在写入----')
        if item['title']:
            # 主要是解决存入csv文件时出现的每一个字以','隔离
            self.writer.writerow((item['title'], item['link'], item['time'], item['category']))
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
