from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo
# Create your views here.


def index(request):
    n = MovieInfo.objects.extra(where=["rate > 3"])
    return render(request, 'comment_list.html', locals())
    # return HttpResponse("hello")


def search(request):
    query = request.GET.get('q')
    err_msg = ''
    if not query:
        err_msg = '请输入关键词'
        return HttpResponse(err_msg)
    post_list = MovieInfo.objects.filter(comment__icontains=query)
    return render(request, 'comment_search_result.html', {'error_msg': err_msg, 'post_list': post_list})
