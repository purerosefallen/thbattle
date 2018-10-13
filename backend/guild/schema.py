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


# ---------------------------
class GuildQuery(gh.ObjectType):
    guilds = gh.Field(Guild, keyword=gh.String(required=True))


class GuildOps(gh.ObjectType):
    create = gh.Field(
        Guild,
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

    join = gh.Boolean(
        guildId=gh.ID(required=True, description="势力ID"),
        required=True,
        description="申请加入势力",
    )

    approve = gh.Boolean(
        playerId=gh.ID(required=True, description="玩家ID"),
        required=True,
        description="批准加入势力",
    )

    kick = gh.Boolean(
        playerId=gh.ID(required=True, description="玩家ID"),
        required=True,
        description="踢出势力",
    )

    quit = gh.Boolean(
        required=True,
        description="退出势力",
    )

    update = gh.Field(
        Guild,
        slogan=gh.String(description="口号"),
        totem=gh.String(description="图腾（URL）"),
        required=True,
        description="更新势力信息",
    )
