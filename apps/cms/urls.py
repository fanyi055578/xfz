from django.urls import path,include
from . import views
from django.conf import  settings
from django.conf.urls.static import static
app_name='cms'

urlpatterns=[
    path('cms/',views.cms_main,name='cms_main'),
    path('cms_news/',views.cms_news,name='cms_news'),
    path('cms_category/',views.cms_category,name='cms_category'),
    path('add_news_category/',views.add_news_category,name='add_news_category'),
    path('edit_news_category/',views.edit_news_category,name='edit_news_category'),
    path('delete_news_category/',views.delete_news_category,name='delete_news_category'),
    path('add_news/',views.add_news,name='add_news'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('course/',views.course,name='course'),
    path('banner/',views.banner,name='banner'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('delete_banner/',views.delete_banner,name='delete_banner'),
    path('pub_course/',views.pub_courses,name='pub_course'),
    path('tests/',views.tests,name='tests'),
    path('delete_news/', views.delete_news, name='delete_news'),
    path('edit_news/', views.edit_news, name='edit_news'),
    path('course_control/',views.course_control,name='course_control'),

]+ static(settings.STATIC_URL,document_root = settings.MEDIA_ROOT)