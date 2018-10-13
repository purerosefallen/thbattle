# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class Item(DjangoObjectType):
    class Meta:
        model = models.Item


class ItemActivity(DjangoObjectType):
    class Meta:
        model = models.ItemActivity


class ExchangeItem(DjangoObjectType):
    class Meta:
        model = models.Exchange


class ExchangeQuery(gh.ObjectType):
    items = gh.List(
        gh.NonNull(ExchangeItem),
        keyword=gh.String(description="关键词"),
        description="搜索交易所",
    )


class Query(object):
    exchange = gh.Field(ExchangeQuery, description="交易所")

    @staticmethod
    def resolve_exchange(root, info):
        return ExchangeQuery()


class ExchangeOps(gh.ObjectType):
    buy    = gh.Field(Item, exchangeItemId=gh.ID(required=True, description="交易条目ID"), description="购买")
    sell   = gh.Field(ExchangeItem, itemId=gh.ID(required=True, description="物品ID"), description="出售")
    cancel = gh.Boolean(exchangeItemId=gh.ID(required=True, description="交易条目ID"), description="取消出售")


class ItemOps(gh.ObjectType):
    add = gh.Field(
        Item,
        to=gh.ID(required=True, description="玩家ID"),
        typ=gh.String(required=True, description="物品类型"),
        reason=gh.String(required=True, description="原因"),
        description="给予玩家一个物品",
    )
    remove = gh.Boolean(
        itemId=gh.ID(required=True, description="物品ID"),
        reason=gh.String(required=True, description="原因"),
        description="移除物品",
    )


class Mutation(object):
    item = gh.Field(ItemOps, description="物品")
    exchange = gh.Field(ExchangeOps, description="交易所")

    @staticmethod
    def resolve_item(root, info):
        return ItemOps()

    @staticmethod
    def resolve_exchange(root, info):
        return ExchangeOps()
