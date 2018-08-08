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


class Query(object):
    item = gh.Field(Item, id=gh.Int())
    exchange = gh.List(ExchangeItem, id=gh.Int())


class Mutation(object):
    pass
