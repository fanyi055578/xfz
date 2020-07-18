from apps.forms import FormMixmin
from django import forms
from apps.course.models import Course
from apps.news.models import News


class PubNews(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title','desc','category','image','content','id']

class EditCategory(forms.Form):

    pk = forms.IntegerField(error_messages={"required":"必须传入id！"})
    name = forms.CharField(max_length=100)


class PubCourseForm(forms.ModelForm, FormMixmin):
    category_id = forms.IntegerField()
    teacher_id = forms.IntegerField()

    class Meta:
        model = Course
        exclude = ("category",'teacher')


class EditNewsForm(forms.ModelForm, FormMixmin):
    category = forms.IntegerField()
    pk = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['category', 'author', 'pub_time']
