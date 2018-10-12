# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType

# -- own --
from . import models
import graphene as gh


# -- code --
class Friend(DjangoObjectType):
    class Meta:
        model = models.Friend


class Block(DjangoObjectType):
    class Meta:
        model = models.Block


# -----------------------------------
class Query(object):
    pass


class FriendOps(gh.ObjectType):
    request = gh.Boolean(id=gh.ID(required=True), description="发起好友请求")
    remove  = gh.Boolean(id=gh.ID(required=True), description="移除好友/拒绝好友请求")
    block   = gh.Boolean(id=gh.ID(required=True), description="拉黑")
    unblock = gh.Boolean(id=gh.ID(required=True), description="解除拉黑")


class Mutation(object):
    friend = gh.Field(FriendOps, description="好友相关操作")

    @staticmethod
    def resolve_friend(root, info):
        return FriendOps()
