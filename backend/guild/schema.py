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


class GuildMember(DjangoObjectType):
    class Meta:
        model = models.GuildMember


class Query(object):
    guild = gh.Field(Guild, id=gh.Int(), name=gh.String())


class Mutation(object):
    pass
