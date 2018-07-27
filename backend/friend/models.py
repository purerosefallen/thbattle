# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib.auth.models import User
from django.db import models

# -- own --


# -- code --
class Friend(models.Model):

    class Meta:
        verbose_name        = '好友关系'
        verbose_name_plural = '好友关系'

    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(User, models.CASCADE, verbose_name='玩家', related_name='+')
    friend  = models.ForeignKey(User, models.CASCADE, verbose_name='好友', related_name='+')
    created = models.DateTimeField('日期', auto_now_add=True)

    # XXX: unique index

    def __str__(self):
        return f'{self.user.username} -> {self.friend.username}'


class Block(models.Model):

    class Meta:
        verbose_name        = '黑名单'
        verbose_name_plural = '黑名单'

    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(User, models.CASCADE, verbose_name='玩家', related_name='+')
    block   = models.ForeignKey(User, models.CASCADE, verbose_name='拉黑', related_name='+')
    created = models.DateTimeField('日期', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -> {self.block.username}'
