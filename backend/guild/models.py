# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib.auth.models import User
from django.db import models

# -- own --


# -- code --
class Guild(models.Model):

    class Meta:
        verbose_name        = '势力'
        verbose_name_plural = '势力'

    id        = models.AutoField(primary_key=True)
    name      = models.CharField('名称', max_length=20, unique=True)
    founder   = models.ForeignKey(User, models.CASCADE, verbose_name='创始人', related_name='founded_guilds')
    leader    = models.ForeignKey(User, models.CASCADE, verbose_name='领袖', related_name='leading_guilds')
    slogan    = models.CharField('口号', max_length=200)
    totem     = models.ImageField('图腾', blank=True)
    foundedAt = models.DateTimeField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name


class GuildMember(models.Model):

    class Meta:
        verbose_name        = '势力成员'
        verbose_name_plural = '势力成员'

    id       = models.AutoField(primary_key=True)
    guild    = models.ForeignKey(Guild, models.CASCADE, verbose_name='势力', related_name='members')
    user     = models.ForeignKey(User, models.CASCADE, verbose_name='成员', related_name='+')
    joinedAt = models.DateTimeField('加入日期', auto_now_add=True)

    def __str__(self):
        return f'{self.guild.name} - {self.member.username}'
