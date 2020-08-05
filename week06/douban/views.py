from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from django.db.models import Avg
from django.core import serializers


# Create your views here.


def index(request):
    # return HttpResponse('douban index')

    # 所有评论
    comments = Comments.objects.all()

    # 星级 > 3
    condition_star = {'stars__gt': 3}
    list_comment = comments.filter(**condition_star)

    count_list = list_comment.count()

    # 评论总数
    count_comment = comments.count()

    # 平均星级
    star_avg = f"{comments.aggregate(Avg('stars'))['stars__avg']:0.1f}"

    # 情感倾向
    sent_avg = f"{comments.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    queryset = comments.values('sentiment')
    # 正向倾向
    condition_sent_good = {'sentiment__gte': 0.5}
    good_sentiment = queryset.filter(**condition_sent_good).count()

    # 负向倾向
    condition_sent_good = {'sentiment__lt': 0.5}
    bad_sentiment = queryset.filter(**condition_sent_good).count()

    return render(request, 'index.html', locals())


def searchcomment(request):
    """
    异步搜索短评
    :param request:
    :return:
    """
    comments = Comments.objects.all()

    if request.method == 'POST':
        search_keyword = request.POST.get('keyword').strip()
        if search_keyword is not None:
            condition_search = {'comment__icontains': search_keyword}
            search_comment = comments.filter(**condition_search)

            result = serializers.serialize('json', search_comment)

            return HttpResponse(result)

    return HttpResponse('Http method not allow')
