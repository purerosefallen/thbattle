# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models

# -- own --

# -- code --
# Create your models here.


class Profile(models.Model):

    class Meta:
        verbose_name        = '玩家资料'
        verbose_name_plural = '玩家资料'

    user     = AutoOneToOneField(User, models.CASCADE, verbose_name='用户')
    phone    = models.BigIntegerField('手机号', unique=True)
    verified = models.BooleanField('已验证', default=False)
    ppoint   = models.IntegerField('P点')
    jiecao   = models.IntegerField('节操')
    games    = models.IntegerField('游戏数')
    drops    = models.IntegerField('逃跑数')
    title    = models.CharField('称号', blank=True, max_length=20)

    def __str__(self):
        return self.user.username


