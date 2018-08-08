# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
from importlib import import_module as M

# -- third party --
# -- own --
import graphene as gh


# -- code --
QUERIES = [
    M('badge.views').Query,
    M('player.views').Query,
    M('friend.views').Query,
    M('guild.views').Query,
    M('item.views').Query,
    M('unlock.views').Query,
    M('system.views').Query,
]


class Query(*QUERIES, gh.ObjectType):
    pass


MUTATIONS = [
    M('badge.views').Mutation,
    M('player.views').Mutation,
    M('friend.views').Mutation,
    M('guild.views').Mutation,
    M('item.views').Mutation,
    M('unlock.views').Mutation,
    M('system.views').Mutation,
]


class Mutation(*MUTATIONS, gh.ObjectType):
    pass


schema = gh.Schema(query=Query, mutation=Mutation)
