# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
import graphene as gh

# -- own --
from graphql import GraphQLError
from django.core.cache import caches


# -- code --
def stub(cls, desc):
    return gh.Field(
        cls,
        resolver=lambda root, info: cls(),
        description=desc,
    )


def require_perm(ctx, perm):
    u = ctx.user
    if not u.has_perm('player.view_user'):
        raise GraphQLError('没有权限')


def rate_limit(token: str, duration: float) -> None:
    c = caches['default']

    if c.get(token):
        raise GraphQLError('请求过于频繁')

    c.set(token, 'rate_limit', duration)
