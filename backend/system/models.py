# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.db import models

# -- own --


# -- code --
class Version(models.Model):

    class Meta:
        verbose_name        = '游戏更新版本数据'
        verbose_name_plural = '游戏更新版本数据'

    id      = models.SlugField('版本', max_length=20, primary_key=True)
    url     = models.FileField('更新文件')
    testing = models.BooleanField('显示测试服入口', default=False)

    def __str__(self):
        return self.id


class News(models.Model):

    class Meta:
        verbose_name        = '新闻'
        verbose_name_plural = '新闻'

    id   = models.AutoField(primary_key=True)
    text = models.TextField('正文')

    def __str__(self):
        return f'News({self.id})'
