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

### Request模拟登陆

- 查看要模拟登陆网站的请求数据格式
- 返回403错误：添加模拟浏览器的头部信息
### Selenium模拟登陆

- 进入登陆页面，找到输入用户名密码框的xpath路径
- 登陆按钮的xpath路径，然后调用click()

