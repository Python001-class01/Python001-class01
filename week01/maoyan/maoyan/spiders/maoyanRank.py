import scrapy
from scrapy.selector import Selector
from ..items import MaoyanItem

class MaoyanrankSpider(scrapy.Spider):
    name = 'maoyanRank'
    allowed_domains = ['m.maoyan.com']
    start_urls = ['http://https://m.maoyan.com/?showType=3#movie/classic/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3&sortId=1'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        counter = 0
        divTags = Selector(response=response).xpath('//dd/div/div[@class="movie-item-hover"]')

        for divTag in divTags:
            if counter <= 10:
                title = divTag.xpath('./a/div/div/span[@class="name "]/text()').extract_first()
                link = divTag.xpath('./a[@data-act="movie-click"]/@href').extract_first()
                category = divTag.xpath('./a/div/div[2]/text()').extract()[1].strip('\n').strip()
                time = divTag.xpath('./a/div/div[4]/text()').extract()[1].strip('\n').strip()

                item = MaoyanItem()
                item['title'] = title
                item['link'] = 'https://maoyan.com' + link
                item['time'] = time
                item['category'] = category
                counter += 1
                yield item
            else:
                yield
