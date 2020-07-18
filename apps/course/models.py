from django.db import models
from shortuuidfield import ShortUUIDField
# Create your models here.


class CourseCategory(models.Model):
    name = models.CharField(max_length=15)


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=15)
    avater = models.URLField()
    jobtitle = models.CharField(max_length=15)
    profile = models.TextField()


class Course(models.Model):
    title = models.CharField(max_length=15, null=True)
    category = models.ForeignKey('CourseCategory',on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher',on_delete=models.DO_NOTHING)
    video_url = models.URLField()
    video_img = models.URLField()
    price = models.FloatField()
    time_lone = models.IntegerField(null=True)
    profile = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)


class CourseOrder(models.Model):
    uid = ShortUUIDField(primary_key=True)
    course = models.ForeignKey("Course",on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey("xfzauth.User",on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0)
    pub_time = models.DateTimeField(auto_now_add=True)
    # 1：代表的是支付宝支付。2：代表的是微信支付
    istype = models.SmallIntegerField(default=0)
    # 1：代表的是未支付。2：代表的是支付成功
    status = models.SmallIntegerField(default=1)


