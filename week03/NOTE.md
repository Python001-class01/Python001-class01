学习笔记

### 多线程主机扫描器
- 处理命令行参数的库argparse
- 执行系统命令（ping）的库subprocess
- 正则表达式判断ip地址
- socket编程
- 多线程-线程池ThreadPoolExecutor

### 多线程requests爬取拉勾网
#### 使用多线程requests的基本爬虫框架
    - 爬虫线程类
    - 数据处理线程类
    - 【未完成】时间关系还未完成保存到数据库这一步
#### 拉勾网页面解析
北上广深四个城市python工程师url：
```
北京
https://www.lagou.com/jobs/list_Python/p-city_2?px=default#filterBox
上海
https://www.lagou.com/jobs/list_Python/p-city_3?px=default#filterBox
广州
https://www.lagou.com/jobs/list_Python/p-city_213?px=default#filterBox
深圳
https://www.lagou.com/jobs/list_Python/p-city_215?px=default#filterBox
```
问题：

- 同一个城市翻页时url没有变化，只做了前端处理
- 返回结果不能直接从response获取，网页异步加载了ajax

职位详情xpath:
```
//*[@id="s_position_list"]/ul/li[i]
```
data-salary字段

##### 翻页问题

post请求，页数由参数pn控制

![error](/Users/h0rs3/Work/学习/python训练营/Python001-class01/week03/picture/lagou翻页.png)

拉勾每页15条职位信息，返回的json中有总数，用总数除以15得到要获取的页数

![error](/Users/h0rs3/Work/学习/python训练营/Python001-class01/week03/picture/totalCount.png)

#### 线程间的通信
