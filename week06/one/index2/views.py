from django.shortcuts import render

# Create your views here.
from .models import Movie2
from django.http import HttpResponse
def movie_short(request):
    #return HttpResponse("rtrtrtrt")
    # 三星级以上
    search_key = request.GET.get('search_input')
    #这个写法，大于，第一次学
    condtions = {'stars__gt': 3}
    if search_key:
        #通过字典，追加过滤条件，where and 
        condtions = {'stars__gt': 3,"shorts__contains": search_key}
    #获取所有行
    #queryset = Movie2.objects.all()
    #而后进行过滤
    good_comment = Movie2.objects.filter(**condtions)
    film_name="肖申克的救赎"
    return render(request, 'result.html', locals())