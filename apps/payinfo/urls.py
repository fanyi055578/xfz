

from django.urls import path,include
from . import views
app_name='payinfo'

urlpatterns = [
    path('', views.payinfo,name='payinfo'),
]
