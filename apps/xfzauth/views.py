from django.shortcuts import render,redirect,reverse
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST
from utils.captcha.xfzcaptcha import Captcha
from io import BytesIO
from utils import restful
from utils.captcha.sendphone import send_telephone
from .models import User
from django.core.cache import cache

# Create your views here.

captcha = []

@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        telephone = form.cleaned_data.get('telephone')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                    return restful.ok()
                else:
                    request.session.set_expiry(0)
                    return restful.ok()
            else:
                return restful.params_error(message="账户已经被东冻结")
        else:
            return restful.params_error(message="错误的账户名或密码")
    else:
        errors = form.get_errors()
        return restful.params_error(errors)


def log(request):
    return render(request,'common/auth.html')


def log_out(request):
    logout(request)
    return redirect(reverse('news:news'))


def image_captcha(request):
    text,image = Captcha.gene_code()
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    print(text)
    cache.set(text.lower(),text.lower(), 5*60)
    captcha.append(text)

    response['Content-length'] = out.tell()
    return response


def send_phone(request):
    tel = request.GET.get('telephone')
    code = Captcha.gene_text()
    cache.set(tel,code,5*60)
    send_telephone(tel,code)
    print(code+'xxxx')
    captcha.append(code)
    cs = cache.get('code')
    print(cs)
    return restful.ok()


def cache_test(request):
    cache.set('username','zhiliao',60)
    result = cache.get('username')
    print(result)
    return HttpResponse('ok')


@require_POST
def Register(requset):
    form = RegisterForm(requset.POST)
    print('ko')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        telephone = form.cleaned_data.get('telephone')
        User.objects.create_user(username=username,password=password1,telephone=telephone)
        return restful.ok()
    else:
        print(form.get_errors())
        return restful.params_error(message=form.get_errors())






    pass















    # codes = captcha[0]
    # ph_codes=captcha[1]
    # code = requset.POST.get('img_captcha')
    # ph_code = requset.POST.get('sms_captcha')
    #
    # if code.lower()!=codes or ph_code.lower()!=ph_codes:
    #     return restful.params_error('图片验证码或手机验证码错误！！')
    # try:
    #     telephone = requset.POST.get('telephone')
    #     username = requset.POST.get('telephone')
    #     password = requset.POST.get('telephone')
    #     User.objects.create_user(telephone=telephone, username=username, password=password)
    #     return restful.ok()
    # except:
    #     return restful.params_error('用户已经存在！')


@require_POST
def add_user_category(request):

    name = request.POST.get('name')










    #
    # form = RegisterForm(requset.POST)
    # if form.is_valid():
    #     username = form.cleaned_data.get('username')
    #     print(username)
    #     telephone = form.cleaned_data.get('telephone')
    #     password = form.cleaned_data.get('password1')
    #     User.objects.create_user(telephone=telephone,username=username,password=password)
    #     return restful.ok()
    # else:
    #     return restful.params_error('非法的数据！')




