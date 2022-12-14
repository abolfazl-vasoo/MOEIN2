# Generated by Django 3.2.14 on 2022-07-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('site_url', models.CharField(max_length=200, verbose_name='دامنه سایت')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت سایت')),
                ('about_us_text', models.TextField(verbose_name='متن درباره ما سایت')),
                ('site_logo', models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('url_title', models.CharField(max_length=200, verbose_name='عنوان لینک')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]
