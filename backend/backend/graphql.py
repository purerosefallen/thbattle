# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
import importlib

# -- third party --
# -- own --
import graphene as gh


# -- code --
QUERIES = [
    importlib.import_module('badge.views').Query,
    importlib.import_module('player.views').Query,
    importlib.import_module('system.views').Query,
]


class Query(*QUERIES, gh.ObjectType):
    pass


MUTATIONS = [
    importlib.import_module('system.views').Mutation,
]


class Mutation(*MUTATIONS, gh.ObjectType):
    pass


schema = gh.Schema(query=Query, mutation=Mutation)
