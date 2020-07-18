from django.db import models

# Create your models here.


class Payinfo(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=40)
    img_url = models.URLField()
    price = models.FloatField(default=0)
