# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.db import models

# -- own --
# -- code --


class Badge(models.Model):

    class Meta:
        verbose_name        = '勋章'
        verbose_name_plural = '勋章'

    id          = models.AutoField(primary_key=True)
    title       = models.CharField('标题', max_length=50, unique=True)
    description = models.CharField('描述', max_length=200)
    icon        = models.ImageField('图标')
    icon2x      = models.ImageField('图标@2x')

    def __str__(self):
        return self.title
