# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class Friend(DjangoObjectType):
    class Meta:
        model = models.Friend


class Block(DjangoObjectType):
    class Meta:
        model = models.Block


class Query(object):
    pass


class Mutation(object):
    pass
