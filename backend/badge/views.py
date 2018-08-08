# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType

# -- own --
from . import models
import graphene as gh


# -- code --
class Badge(DjangoObjectType):
    class Meta:
        model = models.BadgeType


class Query(object):
    badges = gh.List(Badge)


class Mutation(object):
    pass
