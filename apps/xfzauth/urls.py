from django.urls import path
from . import models
from . import views
app_name = 'xfzauth'

urlpatterns=[
   path('login/',views.login_view,name='login'),
   path('lg/',views.log,name='log'),
   path('logout/',views.log_out,name='logout'),
   path('img_capture/',views.image_captcha,name='img_capture'),
   path('send_phone/',views.send_phone,name='send_phone'),
   path('cache/',views.cache_test,name='cache_test'),
   path('register/',views.Register,name='register'),
   path('cache_test/',views.cache_test,name='cache_test'),
]