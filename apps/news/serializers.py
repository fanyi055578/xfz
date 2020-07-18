from rest_framework import  serializers
from .models import News,Category,Comment
from apps.xfzauth.serializers import UserSerializer


class NewsCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategory()
    author = UserSerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'pub_time', 'category','desc','author')


class CommentSerizlizer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id','content','author','pub_time')