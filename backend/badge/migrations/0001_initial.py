# Generated by Django 2.1.2 on 2018-10-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='标题')),
                ('description', models.CharField(max_length=200, verbose_name='描述')),
                ('icon', models.ImageField(upload_to='', verbose_name='图标')),
                ('icon2x', models.ImageField(upload_to='', verbose_name='图标@2x')),
            ],
            options={
                'verbose_name': '勋章',
                'verbose_name_plural': '勋章',
            },
        ),
    ]
