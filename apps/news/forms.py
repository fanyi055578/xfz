from django import forms

from .models import Comment
from ..forms import FormMixmin

class ComentForm(forms.Form,FormMixmin):
    comment = forms.CharField()
    news_id = forms.IntegerField()