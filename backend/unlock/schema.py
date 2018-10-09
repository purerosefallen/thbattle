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


class Query(object):
    pass


class Mutation(object):
    pass
