from django.shortcuts import render,redirect,reverse
from ..news.models import Category,News,Banner
from utils import restful
from django.views.decorators.http import require_POST,require_GET
from .forms import EditCategory,PubCourseForm,PubNews
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
from apps.course.models import Teacher,CourseCategory,Course


# Create your views here.
def index(request):

    return render(request, 'cms/login.html', )


def cms_main(request):

    return render(request, 'adminLTE/index_main.html')


def cms_news(request):
    categorys = Category.objects.all()
    context ={
        'categorys':categorys,
    }

    return render(request, 'adminLTE/index_news.html',context=context)

@require_GET
def cms_category(request):
    categorys = Category.objects.all()
    print(categorys)
    context = {
        'categorys': categorys,
    }

    return render(request, 'adminLTE/index_category.html', context=context)


@require_POST
def add_news_category(request):
    name = request.POST.get('name')
    print(name)
    exists = Category.objects.filter(name=name)
    if exists:
        return restful.params_error('分类已经存在！')
    else:
        Category.objects.create(name=name)
        print('ok')
        return restful.ok()


@require_POST
def edit_news_category(request):
    form = EditCategory(request.POST)

    if form.is_valid():
        try:
            pk=form.cleaned_data.get('pk')
            name = form.cleaned_data.get('name')
            Category.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error('分布没有')
    else:
        return restful.params_error('改分类不存在！')


@require_POST
def delete_news_category(request):
    pk = request.POST.get('pk')
    try:
        Category.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.unauth(message='分类不存在！')


def add_news(request):
    form = PubNews(request.POST)
    print('xxxxxxxxxxxxxxxxxxxxx')
    if form.is_valid():
        print('xxxx')
        title = form.cleaned_data.get('title')
        desc = form.cleaned_data.get('desc')
        category = form.cleaned_data.get('category')
        print(category.id)
        content = form.cleaned_data.get('content')
        img_url = form.cleaned_data.get('image')
        News.objects.create(title=title,desc=desc ,content=content, image=img_url, category_id=category.id)
        return restful.ok()
    else:
        return restful.params_error('参数错误！')


def upload_file(request):
    file = request.FILES.get('file')
    name = file.name
    with open(os.path.join(settings.MEDIA_ROOT,name),'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = request.build_absolute_uri(settings.MEDIA_URL+name)
    return restful.result(data={'url':url})


def banner(request):
    banners = Banner.objects.all()

    print(banners)
    context = {
        'banners': banners
    }
    return render(request, 'adminLTE/banner.html',context=context)


def add_banner(request):
    img_url = request.POST.get('image_url')
    priority = request.POST.get('priority')
    link_to = request.POST.get('link_to')
    pk = request.POST.get('pk')
    Banner.objects.create(image_url=img_url, priority=priority,link_to=link_to, pk=pk)
    return restful.result(data={"banner_id": pk})


def delete_banner(request):
    bannerid = request.POST.get('banner_id')
    Banner.objects.filter(pk=bannerid).delete()

    return restful.ok()


def course(requset):
    course_category = CourseCategory.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'categories':course_category,
        'teachers':teacher,
    }

    return render(requset, 'adminLTE/pub_course.html',context=context)



def pub_courses(request):

    title = request.POST.get('title')
    category_id = request.POST.get('category_id')
    video_url = request.POST.get('video_url')
    cover_url = request.POST.get('cover_url')
    price = request.POST.get('price')
    duration = request.POST.get('duration')
    profile = request.POST.get('profile')
    teacher_id = request.POST.get('teacher_id')
            #
            # category = CourseCategory.objects.get(pk=category_id)
            # teacher = Teacher.objects.get(pk=teacher_id)

    Course.objects.create(title=title, video_url=video_url, video_img=cover_url, price=price,
                                  profile=profile, category_id=category_id, teacher_id=teacher_id)
    return restful.ok()


from .forms import EditNewsForm


def tests(request):
    form = EditNewsForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            Category.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='该分类不存在！')
    else:
        return restful.params_error(message=form.get_errors())


def course_control(request):
    news = News.objects.all()
    return render(request, 'adminLTE/index2.html',locals())


def delete_news(request):
    news_id = request.POST.get('pk')
    News.objects.filter(id=news_id).delete()
    return restful.ok()


def edit_news(request):
     pk = request.GET.get('pk')
     news = News.objects.get(id=pk)
     categorys = Category.objects.all()
     return render(request,'adminLTE/edit_news.html',locals())






