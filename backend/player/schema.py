# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import django.contrib.auth.models as auth_models
import graphene as gh

# -- own --
from . import models


# -- code --
class User(DjangoObjectType):
    class Meta:
        model = auth_models.User
        exclude_fields = [
            'password',
            'last_login',
            'is_superuser',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'date_joined',
        ]


class Group(DjangoObjectType):
    class Meta:
        model = auth_models.Group


class Permission(DjangoObjectType):
    class Meta:
        model = auth_models.Permission


class Profile(DjangoObjectType):
    class Meta:
        model = models.Profile
        exclude_fields = [
            'phone',
        ]


class Query(object):
    user = gh.Field(User, id=gh.Int(), username=gh.String())


class Mutation(object):
    pass
