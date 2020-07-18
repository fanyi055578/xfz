
from django.contrib import admin
from django.urls import path,include
from . import views
app_name='course'

urlpatterns = [
    path('index/',views.course_index,name='index' ),
    path('detail/<course_id>',views.course_detail,name='detail'),
    path('pub_course/',views.Pub_Corese,name="Pub_Corese"),
    path('course_token/',views.course_token,name="course_token"),
    path('course_order/<course_id>',views.course_order,name="course_order"),

]
