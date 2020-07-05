import scrapy
from proxy.items import ProxyItem
import lxml.etree

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']
    header = {
            'Content-Type': 'text/plain; charset=UTF-8',
            'Cookie' : '__mta=251934006.1593072991075.1593315374931.1593349407197.45; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; __mta=251934006.1593072991075.1593140975947.1593145813576.21; mojo-session-id={"id":"afe2ef89c10d6e1c8fc94e26d831b20e","time":1593349078441}; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593349407; _lxsdk_s=172fb017d51-4c4-303-783%7C%7C8',
            # 'Host' : 'http://www.baidu.com',
            'Origin': 'https://maoyan.com',
            'Referer': 'https://maoyan.com/board/4',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }

    # def parse(self, response):
        # pass
    def start_requests(self):

        url = f'https://maoyan.com/board/4'
        yield scrapy.Request(url=url,headers=self.header,callback=self.parse)

    def parse(self, response):
        selector = lxml.etree.HTML(response.text)
        item =ProxyItem()
        for i in range(0,10):
            link = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd['+i+']/div/div/div[1]/p[1]/a').get('href')
            name = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd['+i+']/div/div/div[1]/p[1]/a').get('title')
            time = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd['+i+']/div/div/div[1]/p[3]').text
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
