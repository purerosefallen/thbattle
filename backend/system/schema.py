# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType

# -- own --
from . import models
import graphene as gh


# -- code --
class Version(DjangoObjectType):
    class Meta:
        model = models.Version


class News(DjangoObjectType):
    class Meta:
        model = models.News


class Setting(DjangoObjectType):
    class Meta:
        model = models.Setting


# ------------------------
class SystemQuery(gh.ObjectType):
    version = gh.Field(Version, id=gh.String())
    setting = gh.String(key=gh.String(required=True, description="设置 Key"), description="获取全局设置")
    news = gh.Field(News)
    game_id = gh.Int(required=True, description="分配游戏ID")


class SystemOps(gh.ObjectType):
    sms_code = gh.Boolean(
        phone=gh.String(required=True, description="手机号"),
        description="请求验证码",
    )
