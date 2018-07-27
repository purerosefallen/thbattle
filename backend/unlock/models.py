# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib.auth.models import User
from django.db import models

# -- own --


# -- code --
class Achievement(models.Model):

    class Meta:
        verbose_name        = '成就'
        verbose_name_plural = '成就'

    id          = models.AutoField(primary_key=True)
    user        = models.ForeignKey(User, models.CASCADE, verbose_name='玩家')
    achievement = models.SlugField('成就', max_length=256)

    def __str__(self):
        return f'{self.user.username} - {self.achievement}'


class Unlocked(models.Model):

    class Meta:
        verbose_name        = '解锁项目'
        verbose_name_plural = '解锁项目'

    id   = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, verbose_name='玩家')
    item = models.SlugField('解锁项目', max_length=256)  # character, skin, showgirl

    def __str__(self):
        return f'{self.user.username} - {self.item}'
