# Generated by Django 2.2.5 on 2019-09-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default='content'),
        ),
        migrations.AlterField(
            model_name='news',
            name='detail',
            field=models.CharField(default='null', max_length=200, null=True),
        ),
    ]
