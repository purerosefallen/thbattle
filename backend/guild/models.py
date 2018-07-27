# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib.auth.models import User
from django.db import models

# -- own --
from badge.models import BadgeType


# -- code --
class Guild(models.Model):

    class Meta:
        verbose_name        = '势力'
        verbose_name_plural = '势力'

    id      = models.AutoField(primary_key=True)
    name    = models.CharField('名称', max_length=20, unique=True)
    founder = models.ForeignKey(User, models.CASCADE, verbose_name='创始人', related_name='+')
    leader  = models.ForeignKey(User, models.CASCADE, verbose_name='领袖', related_name='+')
    slogan  = models.CharField('口号', max_length=200)
    totem   = models.ImageField('图腾', blank=True)
    created = models.DateTimeField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name


class GuildMember(models.Model):

    class Meta:
        verbose_name        = '势力成员'
        verbose_name_plural = '势力成员'

    id     = models.AutoField(primary_key=True)
    guild  = models.ForeignKey(Guild, models.CASCADE, verbose_name='势力')
    member = models.ForeignKey(User, models.CASCADE, verbose_name='成员')
    joined = models.DateTimeField('加入日期', auto_now_add=True)

    def __str__(self):
        return f'{self.guild.name} - {self.member.username}'


class GuildBadge(models.Model):

    class Meta:
        verbose_name        = '势力勋章'
        verbose_name_plural = '势力勋章'

    id      = models.AutoField(primary_key=True)
    guild   = models.ForeignKey(Guild, models.CASCADE, verbose_name='所有势力')
    type    = models.ForeignKey(BadgeType, models.CASCADE, verbose_name='勋章')
    created = models.DateTimeField('日期', auto_now_add=True)

    def __str__(self):
        return f'{self.guild.name} - {self.type.title}'
