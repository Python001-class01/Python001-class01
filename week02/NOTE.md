学习笔记

## 第二周知识点小结

### 下载中间件

#### 如何编写一个下载中间件？

一般需要重写四个主要方法：

1. process_request(request, spider)

   Request对象经过下载中间件时会被调用，优先级高先被调用

2. process_response(request, response, spider)

   Response对象经过下载中间件时会被调用，优先级高后被调用

3. process_exception(request, exception, spider)

   当process_response()和process_request()抛出异常时会被调用

4. from_crawler(cls, crawler)

   使用crawler来创建中间器对象初始化信息，并（必须）返回一个中间件对象



### 分布式爬虫

Scrapy原生不支持分布式，多机之间需要Redis实现队列和管道的共享。

scrapy-redis很好地实现了Scrapy和Redis的集成。

#### 使用scrapy-redis之后Scrapy的主要变化：

1. 使用了RedisSpider类替代了Spider类
2. Scheduler的queue由Redis实现
3. item pipeline由Redis实现



### 作业一

没能做出来，参考了别人的答案，还是没能正确实现，相关知识学习还不够，希望老师可以给一份标准答案吧，有个学习参考的模板。



### 作业二

比较简单，跟着课程内容就很容易把题目解决。selenium模拟用户对页面进行操作非常方便，上手比较容易。