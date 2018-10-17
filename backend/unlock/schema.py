# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class Achievement(DjangoObjectType):
    class Meta:
        model = models.Achievement


class Unlocked(DjangoObjectType):
    class Meta:
        model = models.Unlocked


class UnlockOps(gh.ObjectType):
    add_unlock = gh.Boolean(
        id=gh.ID(required=True, description="用户ID"),
        item=gh.String(required=True, description="解锁项目代码"),
        description="解锁项目",
    )

    add_achievement = gh.Boolean(
        id=gh.ID(required=True, description="用户ID"),
        achievement=gh.String(required=True, description="成就代码"),
        description="增加成就",
    )
