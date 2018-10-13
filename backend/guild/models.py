# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from player.models import Player
from django.db import models

# -- own --


# -- code --
class Guild(models.Model):

    class Meta:
        verbose_name        = '势力'
        verbose_name_plural = '势力'

    id         = models.AutoField(primary_key=True)
    name       = models.CharField('名称', max_length=20, unique=True)
    founder    = models.ForeignKey(Player, models.CASCADE, verbose_name='创始人', related_name='founded_guilds')
    leader     = models.OneToOneField(Player, models.CASCADE, unique=True, verbose_name='领袖', related_name='leading_guild')
    slogan     = models.CharField('口号', max_length=200)
    totem      = models.ImageField('图腾', blank=True)
    badges     = models.ManyToManyField('badge.Badge', related_name='guilds', verbose_name='勋章')
    requests   = models.ManyToManyField('player.Player', related_name='requested_guilds', verbose_name='申请列表')
    founded_at = models.DateTimeField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name
