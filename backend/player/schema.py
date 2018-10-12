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
        model = models.User
        exclude_fields = [
            'password',
        ]


class Group(DjangoObjectType):
    class Meta:
        model = auth_models.Group


class Permission(DjangoObjectType):
    class Meta:
        model = auth_models.Permission


class Player(DjangoObjectType):
    class Meta:
        model = models.Player
        exclude_fields = [
            'phone',
        ]


class Credit(DjangoObjectType):
    class Meta:
        model = models.Credit


class Query(object):
    user = gh.Field(User, id=gh.Int(), username=gh.String())

    @staticmethod
    def resolve_user(root, info, id=None, username=None):
        if id is not None:
            return models.User.objects.get(id=id)
        elif username is not None:
            return models.User.objects.get(username=username)

        return None


class Register(gh.Mutation):
    class Arguments:
        username = gh.String(required=True)
        phone    = gh.String(required=True)
        smscode  = gh.Int(required=True)

    token = gh.String(required=True)

    @staticmethod
    def mutate(root, info, username, phone, smscode):
        return Register(token=f'{username}-{phone}-{smscode}')


class RequestSMSCode(gh.Mutation):
    class Arguments:
        phone = gh.Int(required=True)

    @staticmethod
    def mutate(root, info, username, phone, smscode):
        return Register(token=f'{username}-{phone}-{smscode}')


class UserOps(gh.ObjectType):
    register = Register.Field()


class Mutation(object):
    user = gh.Field(UserOps)

    @staticmethod
    def resolve_user(root, info):
        return UserOps()
