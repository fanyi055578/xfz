from .models import Course
from django import forms


class PubCourse(forms.ModelForm):

    class Meta:
        model = Course
        fields = ["title","category","teacher","video_url","video_img","price","time_lone","profile"]

