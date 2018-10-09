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
class NextGameId(gh.Mutation):
    class Arguments:
        pass

    id = gh.Int()

    def mutate(self, info):
        pass


class Query(object):
    version = gh.Field(Version, id=gh.String())
    news = gh.Field(News)


class Mutation(object):
    next_game_id = NextGameId.Field()
