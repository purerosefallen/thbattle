# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib.auth.models import User
from django.db import models

# -- own --


# -- code --
class BadgeType(models.Model):

    class Meta:
        verbose_name        = '勋章类型'
        verbose_name_plural = '勋章类型'

    id          = models.AutoField(primary_key=True)
    title       = models.CharField('标题', max_length=50, unique=True)
    description = models.CharField('描述', max_length=200)
    icon        = models.ImageField('图标')
    icon2x      = models.ImageField('图标@2x')

    def __str__(self):
        return self.title


class Badge(models.Model):

    class Meta:
        verbose_name        = '勋章'
        verbose_name_plural = '勋章'

    id      = models.AutoField(primary_key=True)
    owner   = models.ForeignKey(User, models.CASCADE, verbose_name='所有者')
    type    = models.ForeignKey(BadgeType, models.CASCADE, verbose_name='勋章')
    created = models.DateTimeField('日期', auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.type.title}'
