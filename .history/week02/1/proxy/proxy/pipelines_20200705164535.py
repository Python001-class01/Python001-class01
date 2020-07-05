# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from proxy.store import StoreInfo


class ProxyPipeline:
    def process_item(self, item, spider):
        # return item
        films_name = item['films_name']
        films_type = item['films_type']
        release_time = item['release_time']
        # print(item)

        # output = f'|{films_name}|\t|{films_type}|\t|{release_time}|\n\n'
        # print(output+'pipleLine')
        # with open('./top10.csv', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        #     article.close()
        # return item
        spls = 'insert films (name, type, releasetime) values('+{films_name}+','+{films_type}
