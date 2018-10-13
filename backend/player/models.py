# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
import re

# -- third party --
from annoying.fields import AutoOneToOneField
from django.db import models
from django.utils import timezone
import django.contrib.auth.models as auth_models

# -- own --


# -- code --
def is_phone_number(value):
    if not isinstance(value, str):
        return False

    return bool(re.match(r'^\+?\d{10,15}$', value))


class UserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given phone, and password.
        """
        if not phone:
            raise ValueError('必须填写手机')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    class Meta:
        verbose_name        = '用户'
        verbose_name_plural = '用户'

    USERNAME_FIELD = 'phone'

    objects = UserManager()

    phone = models.CharField('手机号', unique=True, max_length=15, validators=[is_phone_number])
    is_staff = models.BooleanField('职员状态', default=False, help_text='是否可以登录后台')
    is_active = models.BooleanField('启用帐号', default=True, help_text='指明用户是否被认为活跃的。以反选代替删除帐号。')
    date_joined = models.DateTimeField('加入日期', default=timezone.now)


class Player(models.Model):

    class Meta:
        verbose_name        = '玩家'
        verbose_name_plural = '玩家'

    user     = AutoOneToOneField(User, models.CASCADE, verbose_name='用户')
    name     = models.CharField('昵称', unique=True, max_length=150)
    forum_id = models.IntegerField('论坛ID', blank=True, null=True, unique=True)
    bio      = models.CharField('签名', blank=True, max_length=150)
    guild    = models.ForeignKey('guild.Guild', models.SET_NULL, related_name='members', verbose_name='势力', blank=True, null=True)
    badges   = models.ManyToManyField('badge.Badge', related_name='players', verbose_name='勋章')
    friends  = models.ManyToManyField('player.Player', related_name='+', verbose_name='好友')
    blocks   = models.ManyToManyField('player.Player', related_name='+', verbose_name='黑名单')

    def __str__(self):
        return self.name


class Credit(models.Model):

    class Meta:
        verbose_name        = '积分'
        verbose_name_plural = '积分'

    player = AutoOneToOneField(Player, models.CASCADE, verbose_name='玩家')
    ppoint = models.IntegerField('P点')
    jiecao = models.IntegerField('节操')
    games  = models.IntegerField('游戏数')
    drops  = models.IntegerField('逃跑数')

    def __str__(self):
        return self.player.name
