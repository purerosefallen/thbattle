# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
from importlib import import_module as M

# -- third party --
# -- own --
import graphene as gh


# -- code --
QUERIES = [
    M('badge.schema').Query,
    M('player.schema').Query,
    M('guild.schema').Query,
    M('item.schema').Query,
    M('unlock.schema').Query,
    M('system.schema').Query,
]


class Query(*QUERIES, gh.ObjectType):
    pass


MUTATIONS = [
    M('badge.schema').Mutation,
    M('player.schema').Mutation,
    M('guild.schema').Mutation,
    M('item.schema').Mutation,
    M('unlock.schema').Mutation,
    M('system.schema').Mutation,
]


class Mutation(*MUTATIONS, gh.ObjectType):
    pass


schema = gh.Schema(query=Query, mutation=Mutation)
