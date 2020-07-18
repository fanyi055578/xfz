from django.db import models

# Create your models here.
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.cache import cache


class Usermanager(BaseUserManager):
    def _create_user(self,telephone,username,password,**kwargs):
        if not username:
            raise ValueError('请输入用户名！')
        if not telephone:
            raise  ValueError('请输入手机号！')
        if not password:
            raise ValueError('请输入密码！')

        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser']=False
        return self._create_user(telephone,username,password,**kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone, username, password, **kwargs)


class User(AbstractBaseUser,PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=20)
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=False)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    data_joined=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELDS = 'email'
    objects =Usermanager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username



