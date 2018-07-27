# Generated by Django 2.0.7 on 2018-07-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='正文')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.SlugField(max_length=20, primary_key=True, serialize=False, verbose_name='版本')),
                ('url', models.FileField(upload_to='', verbose_name='更新文件')),
                ('testing', models.BooleanField(default=False, verbose_name='显示测试服入口')),
            ],
            options={
                'verbose_name': '游戏更新版本数据',
                'verbose_name_plural': '游戏更新版本数据',
            },
        ),
    ]
