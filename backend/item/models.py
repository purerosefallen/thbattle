# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.db import models
from django.contrib.auth.models import User

# -- own --


# -- code --
class Item(models.Model):

    class Meta:
        verbose_name        = '道具'
        verbose_name_plural = '道具'

    id     = models.AutoField(primary_key=True)
    owner  = models.ForeignKey(User, models.CASCADE, verbose_name='所有者')
    type   = models.SlugField('类型', max_length=20)
    arg    = models.IntegerField('参数', default=0)
    status = models.SlugField('类型', max_length=20)  # backpack, exchange, used

    def __str__(self):
        return f'[{self.id}] {self.type}:{self.arg}'


class ItemActivity(models.Model):

    class Meta:
        verbose_name        = '道具动作历史'
        verbose_name_plural = '道具动作历史'

    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(User, models.CASCADE, verbose_name='相关用户')
    action  = models.SlugField('动作', max_length=20)
    item    = models.ForeignKey(Item, models.CASCADE, verbose_name='道具')
    extra   = models.CharField('额外数据', max_length=256)
    created = models.DateTimeField('日期', auto_now_add=True)

    def __str__(self):
        return self.id


class Exchange(models.Model):

    class Meta:
        verbose_name        = '交易中的道具'
        verbose_name_plural = '交易中的道具'

    id     = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, models.CASCADE, verbose_name='卖家')
    item   = models.ForeignKey(Item, models.CASCADE, verbose_name='道具')
    price  = models.PositiveIntegerField('价格')

    def __str__(self):
        return f'[{self.id}] {self.item.type}'
