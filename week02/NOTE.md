学习笔记
### 使用Mysql保存爬虫结果
- Mysql的安装使用
- Mysql中基本的数据库、表创建，数据增删改查操作
- 使用pymysql与Mysql交互

### Scrapy自定义中间件实现代理IP
- Scrapy框架中中间件的作用
- settings.py中关于中间件的设置
- Scrapy内置中间件类的实现框架
    - process_request
    
    - process_response
    
    - process_exception
    
    - from_crawle  **classmethod**
    
    - _set_proxy
    
- 类的继承

### Scrapy代理问题

代理设置未生效：

直接使用了示例的http代理，而猫眼是https协议，在`HttpProxyMiddleware`的`process_request`中
```python
parsed = urlparse_cached(request)
# 请求的网站的协议
scheme = parsed.scheme

# 'no_proxy' is only supported by http schemes
if scheme in ('http', 'https') and proxy_bypass(parsed.hostname):
    return

# 检查请求网站的协议是否在设置的代理协议中，否则不会调用_set_proxy
if scheme in self.proxies:
    self._set_proxy(request, scheme)
```
解决方法：

1. settings.py中设置https的协议

2. 重写process_request

### Request模拟登陆

- 查看要模拟登陆网站的请求数据格式
- 返回403错误：添加模拟浏览器的头部信息
### Selenium模拟登陆

- 进入登陆页面，找到输入用户名密码框的xpath路径
- 登陆按钮的xpath路径，然后调用click()

