# Generated by Django 3.2.14 on 2022-07-28 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creat_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2022, 7, 28), verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
    ]
