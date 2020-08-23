import scrapy
from proxy.items import ProxyItem
i,

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
        # pass
    def start_requests(self):

        url = f'https://maoyan.com/board/4'
        yield scrapy.Request(url=url,headers=self.header,callback=self.parse)

    def parse(self, response):
        selector = lxml.etree.HTML(response.text)
        item =ProxyItem()
        for i in range(0,10):
            link = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[i]/div/div/div[1]/p[1]/a').get('href')
            name = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[i]/div/div/div[1]/p[1]/a').get('title')
            time = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[i]/div/div/div[1]/p[3]').text
            item['films_name'] = name
            item['release_time'] = time
            print(link) 
            yield scrapy.Request(url=link, headers = self.header, meta={'item':item},callback=self.parse1)


    def parse1(self, response):
        item = response.meta['item']
        selector = lxml.etree.HTML(response.text)
        type =  selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]').text.replace('\n',' ')
        print(type)
        item['films_type'] = type
        print(item)
        yield item
