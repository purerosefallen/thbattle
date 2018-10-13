# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from player.models import Player
from django.db import models

# -- own --


# -- code --
class Friend(models.Model):

    class Meta:
        verbose_name        = '好友关系'
        verbose_name_plural = '好友关系'
        unique_together = [
            ['player', 'friend'],
        ]

    id          = models.AutoField(primary_key=True)
    player      = models.ForeignKey(Player, models.CASCADE, verbose_name='玩家', related_name='friends')
    friend      = models.ForeignKey(Player, models.CASCADE, verbose_name='好友', related_name='+')
    followed_at = models.DateTimeField('日期', auto_now_add=True)

    def __str__(self):
        return f'{self.player.user.username} -> {self.friend.user.username}'


class Block(models.Model):

    class Meta:
        verbose_name        = '黑名单'
        verbose_name_plural = '黑名单'
        unique_together = [
            ['player', 'block'],
        ]

    id         = models.AutoField(primary_key=True)
    player     = models.ForeignKey(Player, models.CASCADE, verbose_name='玩家', related_name='blocks')
    block      = models.ForeignKey(Player, models.CASCADE, verbose_name='拉黑', related_name='+')
    blocked_at = models.DateTimeField('日期', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -> {self.block.username}'
