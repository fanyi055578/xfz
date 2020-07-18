from django.shortcuts import render
from .models import Category
from .models import News,Banner,Category,Comment
from django.conf import settings
from utils import restful
from django.http import  HttpResponse
from .serializers import NewsSerializer,CommentSerizlizer
from .forms import ComentForm
from django.db.models import Q
from django.views.decorators.http import require_POST,require_GET

# Create your views here.


def news(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.order_by('pub_time')[0:count]
    banners = Banner.objects.all()
    categorys = Category.objects.all()
    context = {
        'newses':newses,
        'banners':banners,
        'categorys':categorys,
    }
    return render(request,'news/index.html',context=context)


@require_GET
def news_list(request):
    page = int(request.GET.get('p', 1))
    category_id =int(request.GET.get('category_id',0))
    start = (page-1)*settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.order_by('id')[start:end]
    else:
        newses = News.objects.filter(category_id=category_id).order_by('id')[start:end]
    serializerz = NewsSerializer(newses, many=True)
    datas = serializerz.data
    print(datas)
    return restful.result(data=datas)


def news_detail(request, news_id=0):
    newses = News.objects.get(id=news_id)
    comment =   Comment.objects.filter(news_id=news_id)
    context = {
        'newses': newses,
        'comments':comment
    }
    return render(request, 'news/news_detail.html',context=context)


def news_comment(request):
    form = ComentForm(request.POST)
    if form.is_valid():
        user_comment = form.cleaned_data.get('comment')
        user_news = form.cleaned_data.get('news_id')
        news_id = News.objects.get(id=user_news)
        author = request.user
        comments = Comment.objects.create(content=user_comment,news=news_id,author=author)
        comment_serizlize = CommentSerizlizer(comments)
        return restful.result(data=comment_serizlize.data)

    else:
        return restful.params_error(message=form.get_errors()) 



def search(request):
    q = request.GET.get('q')
    print(q)
    context = {}
    if q:
        newses = News.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
        context = {'newses':newses}
    print(context)
    return render(request, 'search/search1.html', context=context)