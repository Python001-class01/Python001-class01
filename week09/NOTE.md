学习笔记

进入第9周，学习非常吃力，
开始的源代码分析，就是听不懂‘
后来的form 表单提交，CSRF 防护，信号，中间件，定时任务，略知一二；
最后，两个，几乎听不懂。

偷看，别人的笔记，如下

二、DjangoWeb部分
1、管理界面： 管理页面的设计哲学：

管理后台是一项缺乏创造性和乏味的工作，Django 全自动地根据模型创建后台界面。
管理界面不是为了网站的访问者，而是为管理者准备的。
后台管理界面：Django服务的ip:端口/admin
创建管理员账号：$ python manage.py createsuperuser

增加模型：

./index/admin.py
from .models import Type, Name
# 注册模型
admin.site.register(Type)
admin.site.register(Name)
注意点：
1)settings.py中必须配置好：

INSTALLED_APPS = [
    ####  内置的后台管理系统
    'django.contrib.admin',
    ...]
否则用不了；
2)引入模型，必须是类名；
3)settings.py数据库配置正确；
4)migrate命令将后台管理需要的表导入指定数据库；

2、表单：
html形式：

<form action="result.html" method="post">
    username:<input type="text" name="username" /><br>
    password:<input type="password" name="password" /> <br>
    <input type="submit" value="登录">
</form>
后台生成形式：
views中调用forms相关校验功能

# form.py
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)

# html：
<form action="/login2" method="post">
{% csrf_token %}
{{ form }}
<input type="submit" value="Login">
</form>

html通过url找到views.py对应的函数使用表单：

# views.py
# 该函数处理两种请求方式，如果是GET，就将表单元素对象返回给页面展示，如果是POST说明是表单提交，做验证逻辑；
def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)  
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})

3、表单CSRF防护：
CSRF:跨站请求攻击
防止CSRF:POST页面添加csrf token : {% csrf_token %}
csrf防护在settings中中间件配置,只对post请求做防护：

MIDDLEWARE = [
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    ...
]
如果只针对个别post请求做csrf防护，可以不需要配置中间件，直接在代码中添加@csrf_protect或@csrf_exempt，具体如下：
@csrf_protect是进行csrf验证，@csrf_exempt是免除csrf验证

from django.views.decorators.csrf import csrf_exempt, csrf_protect
@csrf_exempt
def result(request):
    return render(request, 'result.html')
如果是ajax请求，也要添加csrf token；

4、用户管理认证：
Django自带了用户认证模块，以及对会话的处理；

首先配置验证中间件：

MIDDLEWARE = [
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]
然后是代码部分，Django用户验证主要用到django.contrib.auth包：一般主要用到login，authenticate，logout

from .form import LoginForm
from django.contrib.auth import authenticate, login
def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            # 验证用户信息
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户 保存会话
                login(request, user)  
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})
需要验证的用户信息，可以通过Django命令行进行创建：

首先进入Django的shell命令控制台：python manage.py shell
导入验证模块：from django.contrib.auth.model import User
然后user = User.objects.create_user('name', 'email', 'password') 语句创建用户实例，user.save()会利用Django自己的ORM在数据库中保存该用户信息，保存到数据库的用户密码会加密；