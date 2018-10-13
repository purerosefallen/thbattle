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

    friend_requests = gh.List(
        gh.NonNull('player.schema.Player'),
        required=True,
        description="未处理的好友请求",
    )

    @staticmethod
    def resolve_friends(root, info):
        '要特殊处理'
        pass


class Credit(DjangoObjectType):
    class Meta:
        model = models.Credit


class Query(object):
    '''
    user = gh.Field(User, id=gh.Int(), username=gh.String())

    @staticmethod
    def resolve_user(root, info, id=None, username=None):
        if id is not None:
            return models.User.objects.get(id=id)
        elif username is not None:
            return models.User.objects.get(username=username)

        return None
    '''


class Register(gh.Mutation):
    class Arguments:
        username = gh.String(required=True)
        phone    = gh.String(required=True)
        smscode  = gh.Int(required=True)

    token = gh.String(required=True, description="登录令牌")
    player = gh.Field(Player, required=True, description="玩家")

    @staticmethod
    def mutate(root, info, username, phone, smscode):
        return Register(token=f'{username}-{phone}-{smscode}')


class Login(gh.Mutation):
    class Arguments:
        id       = gh.ID(description="用户ID")
        forum_id = gh.ID(description="论坛用户ID")
        phone    = gh.String(description="手机")
        name     = gh.String(description="昵称")
        password = gh.String(required=True, description="密码")

    token = gh.String(required=True, description="登录令牌")

    @staticmethod
    def mutate(root, info):
        pass


class PlayerOps(gh.ObjectType):
    login    = Login.Field(description="登录")
    register = Register.Field(description="注册")
    update = gh.Field(
        Player,
        bio=gh.String(description="签名"),
        required=True,
        description="更新资料",
    )
    bind_forum = gh.Field(
        Player,
        forum_id=gh.ID(required=True, description="论坛UID"),
        forum_password=gh.String(required=True, description="论坛密码"),
        description="绑定论坛帐号",
    )


class FriendOps(gh.ObjectType):
    request = gh.Boolean(id=gh.ID(required=True), description="发起好友请求")
    remove  = gh.Boolean(id=gh.ID(required=True), description="移除好友/拒绝好友请求")
    block   = gh.Boolean(id=gh.ID(required=True), description="拉黑")
    unblock = gh.Boolean(id=gh.ID(required=True), description="解除拉黑")


class Mutation(object):
    player = gh.Field(PlayerOps, description="用户/玩家")
    friend = gh.Field(FriendOps, description="好友相关操作")

    @staticmethod
    def resolve_user(root, info):
        return PlayerOps()

    @staticmethod
    def resolve_friend(root, info):
        return FriendOps()
