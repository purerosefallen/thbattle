# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class Guild(DjangoObjectType):
    class Meta:
        model = models.Guild

    joined_at = gh.DateTime(description="玩家加入日期（只在特定情况有效）")


# ---------------------------
class GuildQuery(gh.ObjectType):
    search = gh.Field(Guild, keyword=gh.String(required=True))


class Query(object):
    guild = gh.Field(GuildQuery, description="势力相关查询")

    @staticmethod
    def resolve_guild(root, info):
        return GuildQuery()


class GuildOps(gh.ObjectType):
    create = gh.Field(Guild,
        name=gh.String(required=True, description="势力名称"),
        slogan=gh.String(required=True, description="势力口号"),
        totem=gh.String(description="势力图腾（图片URL）"),
        required=True,
        description="创建势力",
    )

    transfer = gh.Boolean(
        guildId=gh.ID(required=True, description="势力ID"),
        to=gh.ID(required=True, description="接收人用户ID"),
        required=True,
        description="转让势力",
    )


class Mutation(object):
    guild = gh.Field(GuildOps, description="势力相关操作")

    @staticmethod
    def resolve_guild(root, info):
        return GuildOps()
