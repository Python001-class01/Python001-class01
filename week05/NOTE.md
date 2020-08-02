学习笔记
### ORM API
创建表 字段类型

### week05作业
使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息：

1. 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；(爬虫)
    - 存40条 爬虫实现翻页
    - 豆瓣短评展开更多由前端实现（直接用scrapy请求该链接会一直重定向），先请求电影详情页面，找到更多短评对应的url再请求新的url并解析内容
2. 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级；
    - Django数据库配置，默认SQLite，换成其他需要安装合适的database bindings
    - pip安装mysqlclient出错（mysql_config not found），原因是在虚拟环境中没有在PATH中指定mysql路径。解决方法是在venv的bin/active下添加`PATH="$PATH:/usr/local/mysql/bin/"`，然后再次`source bin/active`
    - 编辑Django的`settings.py`中的数据库配置 `DATABASES`
    - 创建app module
    - 应用comment的models中创建comment和rate两个字段
    - views.py 星级的筛选：`n = MovieInfo.objects.extra(where=["rate > 3"])`
3. （选做)）在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。
    - html前端搜索表单
    - app的urlpattern中增加search的url，并指向views.search
    - app目录下的view.py实现`def search(request)`方法，解析参数
    - 通过`MovieInfo.objects.filter(comment__icontains=query)`筛选