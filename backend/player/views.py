# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType

# -- own --
from . import models
import graphene as gh
import django.contrib.auth.models as auth_models


# -- code --
class User(DjangoObjectType):
    class Meta:
        model = auth_models.User


class Group(DjangoObjectType):
    class Meta:
        model = auth_models.Group


class Permission(DjangoObjectType):
    class Meta:
        model = auth_models.Permission


class Profile(DjangoObjectType):
    class Meta:
        model = models.Profile


class Query(object):
    profile = gh.Field(Profile, id=gh.Int(), name=gh.String())

# Create your views here.
