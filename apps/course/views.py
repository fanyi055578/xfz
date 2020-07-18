from django.shortcuts import render
from .models import Course,CourseOrder
from django import views
from .forms import PubCourse
from utils import restful
import time,hmac,os,hashlib
from django.conf import settings

# Create your views here.


def course_index(request):
    contexts = Course.objects.all()
    context = {
        'Courses':contexts,
    }
    return render(request,'course/course_index.html',context=context)


def course_detail(request,course_id):
    coursess = Course.objects.get(pk=course_id)
    context = {
        'course':coursess,
    }
    return render(request,'course/course_detail.html',context=context)


def Pub_Corese(request):
    form = PubCourse(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        category = form.cleaned_data.get('category')
        teacher = form.cleaned_data.get('teacher')
        video_url = form.cleaned_data.get('video_url')
        video_img = form.cleaned_data.get('video_img')
        price = form.cleaned_data.get('price')
        time_lone = form.cleaned_data.get('time_long')
        profile = form.cleaned_data.get('profile')
        Course.objects.create(title=title,teacher=teacher,category=category,video_url=video_url,video_img=video_img,
                              price=price,time_lone=time_lone,profile=profile)
        return restful.ok()
    else:
        print(form.errors)
        return restful.params_error(form.errors)


def course_token(request):
    # video：是视频文件的完整链接
    file = request.GET.get('video')
    # course_id = request.GET.get('course_id')
    # if not CourseOrder.objects.filter(course_id=course_id,buyer=request.user,status=2).exists():
    #     return restful.params_error(message='请先购买课程！')

    expiration_time = int(time.time()) + 2 * 60 * 60

    USER_ID = settings.BAIDU_CLOUD_USER_ID
    USER_KEY = settings.BAIDU_CLOUD_USER_KEY

    # file=http://hemvpc6ui1kef2g0dd2.exp.bcevod.com/mda-igjsr8g7z7zqwnav/mda-igjsr8g7z7zqwnav.m3u8
    extension = os.path.splitext(file)[1]
    media_id = file.split('/')[-1].replace(extension, '')

    # unicode->bytes=unicode.encode('utf-8')bytes
    key = USER_KEY.encode('utf-8')
    message = '/{0}/{1}'.format(media_id, expiration_time).encode('utf-8')
    signature = hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()
    token = '{0}_{1}_{2}'.format(signature, USER_ID, expiration_time)
    return restful.result(data={'token': token})


def course_order(request,course_id):
    goods = Course.objects.get(pk=course_id)
    context={
        'goods':goods
    }
    return render(request,'course/course_order.html', context=context)