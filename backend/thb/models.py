# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib.auth.models import AbstractUser
from django.db import models
from annoying.fields import AutoOneToOneField

# -- own --

# -- code --
# Create your models here.


class User(AbstractUser):
    phone    = models.BigIntegerField('手机号', unique=True)
    verified = models.BooleanField('已验证', default=False)

    REQUIRED_FIELDS = ['email', 'phone']


class Profile(models.Model):

    class Meta:
        verbose_name        = '用户资料'
        verbose_name_plural = '用户资料'

    user   = AutoOneToOneField(User, models.CASCADE, verbose_name='用户')
    ppoint = models.IntegerField('P点')
    jiecao = models.IntegerField('节操')
    games  = models.IntegerField('游戏数')
    drops  = models.IntegerField('逃跑数')
    title  = models.CharField('称号', blank=True, max_length=20)

    def __str__(self):
        return self.user.username


class Item(models.Model):

    class Meta:
        verbose_name        = '道具'
        verbose_name_plural = '道具'

    id     = models.AutoField(primary_key=True)
    owner  = models.ForeignKey(User, models.CASCADE, verbose_name='所有者')
    type   = models.CharField('类型', max_length=20)
    arg    = models.IntegerField('参数', default=0)
    status = models.CharField('类型', max_length=20)  # backpack, exchange, used

    def __str__(self):
        return f'[{self.id}] {self.type}:{self.arg}'


class ItemActivity(models.Model):

    class Meta:
        verbose_name        = '道具动作历史'
        verbose_name_plural = '道具动作历史'

    id      = models.AutoField(primary_key=True)
    user    = models.ForeignKey(User, models.CASCADE, verbose_name='相关用户')
    action  = models.CharField('动作', max_length=20)
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


class Achievement(models.Model):

    class Meta:
        verbose_name        = '成就'
        verbose_name_plural = '成就'

    id          = models.AutoField(primary_key=True)
    user        = models.ForeignKey(User, models.CASCADE, verbose_name='玩家')
    achievement = models.CharField('成就', max_length=256)

    def __str__(self):
        return f'{self.user.username} - {self.achievement}'


class Unlocked(models.Model):

    class Meta:
        verbose_name        = '解锁项目'
        verbose_name_plural = '解锁项目'

    id   = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, verbose_name='玩家')
    item = models.CharField('解锁项目', max_length=256)  # character, skin, showgirl

    def __str__(self):
        return f'{self.user.username} - {self.item}'


class Version(models.Model):

    class Meta:
        verbose_name        = '游戏更新版本数据'
        verbose_name_plural = '游戏更新版本数据'

    id      = models.CharField('版本', max_length=20, primary_key=True)
    url     = models.URLField('更新URL')
    testing = models.BooleanField('显示测试服入口', default=False)

    def __str__(self):
        return self.id


class BadgeType(models.Model):

    class Meta:
        verbose_name        = '勋章类型'
        verbose_name_plural = '勋章类型'

    id          = models.AutoField(primary_key=True)
    title       = models.CharField('标题', max_length=50, unique=True)
    description = models.CharField('描述', max_length=200)
    icon        = models.URLField('图标URL')
    icon2x      = models.URLField('图标@2xURL')

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


class Guild(models.Model):

    class Meta:
        verbose_name        = '势力'
        verbose_name_plural = '势力'

    id        = models.AutoField(primary_key=True)
    name      = models.CharField('名称', max_length=20, unique=True)
    founder   = models.ForeignKey(User, models.CASCADE, verbose_name='创始人', related_name='+')
    president = models.ForeignKey(User, models.CASCADE, verbose_name='主席', related_name='+')
    slogan    = models.CharField('口号', max_length=200)
    totem     = models.URLField('图腾', blank=True)
    created   = models.DateTimeField('创建日期', auto_now_add=True)

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


class News(models.Model):

    class Meta:
        verbose_name        = '新闻'
        verbose_name_plural = '新闻'

    id   = models.AutoField(primary_key=True)
    text = models.TextField('正文')

    def __str__(self):
        return f'News({self.id})'


'''
class Showgirl(Model):
    __tablename__ = 'showgirl'

    id       = Column(Integer, primary_key=True)
    uid      = Column(Integer, nullable=False)
    girl_sku = Column(String(64), nullable=False)  # full-qualified-name
    mood     = Column(Integer, nullable=False)     # 心情，max 10，每天下降 1，摸一次头涨 2，每天一次
    food     = Column(Integer, nullable=False)     # 饥饿，max 30，每天下降1，喂一个物品涨 5 。

    # 两个都归零看板娘会跑掉！

Live
    Servers
        OnlineUsers
        Games
        [DisableAya]
        [DisableMaoyuLogin]

News
    Unread

Game
    Id
    Title
    Players
    Winners
    Replay

Match
    Title
    Game
'''
