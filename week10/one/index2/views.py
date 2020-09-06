from django.shortcuts import render

# Create your views here.
from .models import Movie2, Zdm_pro_com
from django.http import HttpResponse
from django.db.models import Avg


def phone_short(request):
    # return HttpResponse("rtrtrtrt")

    # 获取用户要搜索的手机品牌
    search_key = request.GET.get('search_input')
    # 这个写法，大于，第一次学
    condtions = {}
    if search_key:
        # 通过字典，追加过滤条件，where and
        condtions = {"band__contains": search_key}
        # 获取所有行
        comments = Zdm_pro_com.objects.filter(**condtions)

        # 评论数量
        counter = comments.count()
        # 情感倾向
        sent_avg = f" {comments.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

        # 正向数量
        queryset = comments.values('sentiment')
        condtions = {'sentiment__gte': 0.5}
        plus = queryset.filter(**condtions).count()

        # 负向数量
        queryset = comments.values('sentiment')
        condtions = {'sentiment__lt': 0.5}
        minus = queryset.filter(**condtions).count()

        # 而后进行过滤
        #good_comment = Movie2.objects.filter(**condtions)
        #good_comment = Zdm_pro_com.objects.filter(**condtions)
        # print(len(good_comment))
        film_name = "手机的舆论分析平台"
        return render(request, 'result.html', locals())

    else:
        # 获取所有行
        comments = Zdm_pro_com.objects.all()
        # 评论数量
        counter = comments.count()
        # 情感倾向
        sent_avg = f" {comments.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

        # 正向数量
        queryset = comments.values('sentiment')
        condtions = {'sentiment__gte': 0.5}
        plus = queryset.filter(**condtions).count()

        # 负向数量
        queryset = comments.values('sentiment')
        condtions = {'sentiment__lt': 0.5}
        minus = queryset.filter(**condtions).count()

        # 而后进行过滤
        #good_comment = Movie2.objects.filter(**condtions)
        #good_comment = Zdm_pro_com.objects.filter(**condtions)
        # print(len(good_comment))
        film_name = "手机的舆论分析平台"
        return render(request, 'result.html', locals())
