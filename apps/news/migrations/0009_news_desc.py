# Generated by Django 2.2 on 2019-10-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='desc',
            field=models.CharField(default='此消息存在', max_length=25),
        ),
    ]
