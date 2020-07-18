from django.db import models
from apps.xfzauth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=10)


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField(default='content')
    pub_time = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=25,default="此消息存在")
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('xfzauth.User',on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['pub_time']


class Banner(models.Model):
    priority = models.IntegerField(default=0)
    image_url = models.URLField()
    link_to = models.URLField()
    pub_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-priority']


class Comment(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey("News",on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey("xfzauth.User",on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_time']