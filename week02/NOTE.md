学习笔记

本周学习时间较少；

对于python 异常处理 以及else 写法，以及with处理文件，都学会了，  
主要是一旦出现多个异常，可用出现某个异常忘记处理，程序的健壮性就有问题了。

对于PyMySQL 来连接，感谢老师，这个经验呀。避免我们踩多少坑。

反爬虫，和反反爬虫，天生一对。  
1、本周老师给了几个方法 1、模拟多个模拟器头部

2、cookies 这个，有时间限制

3、webdriver 模拟行为


4、验证码识别，

5、更换代理ip

6、最关键的是分布式爬虫，

老师能够快速的找到需要继承的地方，需要重写的方法，注意之间参数格式的遵守，用字典

我还是需要再多看几遍，路漫漫。



对于作业2 ，由于时间紧，直接把文件shimo_login.py 放到了
G:\geek\Python001-class01\week02\vvv\Scripts 目录下了， 当然
chromedriver.exe 也是放在这里，运行成功，抓了图。


---
作业一，当时命令执行情况
E:\gaodi\Python001-class01\week02\spiders\spiders\spiders> scrapy crawl movies
2020-07-14 18:45:19 [scrapy.utils.log] INFO: Scrapy 2.1.0 started (bot: spiders)
2020-07-14 18:45:19 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.6.0, w3lib 
1.21.0, Twisted 20.3.0, Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1g  21 Apr 2020), cryptography 2.9.2, Platform Windows-10-10.0.18362-SP0
2020-07-14 18:45:19 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-07-14 18:45:19 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'spiders',
 'DOWNLOAD_DELAY': 1,
 'NEWSPIDER_MODULE': 'spiders.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['spiders.spiders'],
 'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/66.0.3359.139 '
               'Safari/537.36Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 '
               '(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'}
2020-07-14 18:45:19 [scrapy.extensions.telnet] INFO: Telnet Password: 79388ff501a276eb
2020-07-14 18:45:20 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2020-07-14 18:45:21 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'spiders.middlewares.RandomHttpProxyMiddleware',
 'spiders.middlewares.SpidersDownloaderMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-07-14 18:45:21 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-07-14 18:45:21 [scrapy.middleware] INFO: Enabled item pipelines:
['spiders.pipelines.SpidersPipeline']
2020-07-14 18:45:21 [scrapy.core.engine] INFO: Spider opened
2020-07-14 18:45:21 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-07-14 18:45:21 [movies] INFO: Spider opened: movies
2020-07-14 18:45:21 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-07-14 18:45:22 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://maoyan.com/robots.txt> (referer: None)
2020-07-14 18:45:23 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://maoyan.com/films?showType=3&sortId=1> (referer: None)
天气之子 爱情／动画／奇幻 2019-11-01
2020-07-14 18:45:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '爱情／动画／奇幻', 'post_time': '2019-11-01', 'title': '天气之子'}
误杀 剧情／犯罪 2019-12-13
2020-07-14 18:45:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '剧情／犯罪', 'post_time': '2019-12-13', 'title': '误杀'}
唐人街探案2 喜剧／动作／悬疑 2018-02-16
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '喜剧／动作／悬疑', 'post_time': '2018-02-16', 'title': '唐人街探案2'}
哪吒之魔童降世 动画／喜剧／奇幻 2019-07-26
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '动画／喜剧／奇幻', 'post_time': '2019-07-26', 'title': '哪吒之魔童降世'}
少年的你 爱情／青春／剧情 2019-10-25
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '爱情／青春／剧情', 'post_time': '2019-10-25', 'title': '少年的你'}
战狼2 动作／战争 2017-07-27
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '动作／战争', 'post_time': '2017-07-27', 'title': '战狼2'}
毒液2 动作／科幻／惊悚／恐怖 2020-06-25
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '动作／科幻／惊悚／恐怖', 'post_time': '2020-06-25', 'title': '毒液2'}
前哨 剧情／历史／战争 2020-06-29
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '剧情／历史／战争', 'post_time': '2020-06-29', 'title': '前哨'}
恐怖电影院2 恐怖／惊悚 2017-10-20
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '恐怖／惊悚', 'post_time': '2017-10-20', 'title': '恐怖电影院2'}
哥斯拉2：怪兽之王 科幻／灾难／动作 2019-05-31
2020-07-14 18:45:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://maoyan.com/films?showType=3&sortId=1>
{'info': '科幻／灾难／动作', 'post_time': '2019-05-31', 'title': '哥斯拉2：怪兽之王'}
2020-07-14 18:45:25 [scrapy.core.engine] INFO: Closing spider (finished)
2020-07-14 18:45:25 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 451,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 12213,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 3.793625,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 7, 14, 10, 45, 25, 226372),
 'item_scraped_count': 10,
 'log_count/DEBUG': 12,
 'log_count/INFO': 11,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2020, 7, 14, 10, 45, 21, 432747)}
2020-07-14 18:45:25 [scrapy.core.engine] INFO: Spider closed (finished)
PS E:\gaodi\Python001-class01\week02\spiders\spiders\spiders>

数据库截图，再发个图片吧
