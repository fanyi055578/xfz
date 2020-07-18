from django import forms
from apps.forms import FormMixmin
from .models import User
from django.core.cache import cache


class LoginForm(forms.Form, FormMixmin):
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=10,min_length=6)
    remember = forms.IntegerField(required=False)


class RegisterForm(forms.Form,FormMixmin):
    telephone = forms.CharField(max_length=11)
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20, min_length=6,
                               error_messages={"max_length": "密码最多不能超过20个字符！", "min_length": "密码最少不能少于6个字符！"})
    password2 = forms.CharField(max_length=20, min_length=6,
                                error_messages={"max_length": "密码最多不能超过20个字符！", "min_length": "密码最少不能少于6个字符！"})
    img_captcha = forms.CharField(min_length=4,max_length=4)
    sms_captcha = forms.CharField(min_length=4,max_length=4)

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1!=password2:
            raise forms.ValidationError('两次输入的密码不一致')

        img_captcha = cleaned_data.get('img_captcha')
        cache_img_captcha = cache.get(img_captcha.lower())

        if not img_captcha or img_captcha != cache_img_captcha:
            raise forms.ValidationError('图形验证码错误!')

        sms_captcha = cleaned_data.get('sms_captcha')
        catch_sms_captcha = cache.get(sms_captcha.lower)

        if not sms_captcha or sms_captcha != catch_sms_captcha:
            raise  forms.ValidationError('手机验证码错误')











