# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.db import transaction
from graphene.utils.props import props
from graphene_django.types import DjangoObjectType
import django.contrib.auth as auth
import django.contrib.auth.models as auth_models
import graphene as gh

# -- own --
from . import models
from graphql import GraphQLError
from utils.graphql import require_perm
import utils.leancloud


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
        description="未处理的好友请求",
    )

    @staticmethod
    def resolve_friends(root, info):
        return root.friends.filter(friends__id=root.id)

    @staticmethod
    def resolve_friend_requests(root, info):
        return root.friends.exclude(
            id__in=root.friends.filter(friends__id=root.id).only('id')
        )


class Credit(DjangoObjectType):
    class Meta:
        model = models.Credit


class PlayerQuery(gh.ObjectType):
    user = gh.Field(
        User,
        id=gh.Int(description="用户ID"),
        phone=gh.String(description="手机号"),
        token=gh.String(description="登录令牌"),
        description="获取用户",
    )

    @staticmethod
    def resolve_user(root, info, id=None, phone=None, token=None):
        ctx = info.context
        require_perm(ctx, 'player.view_user')

        if id is not None:
            return models.User.objects.get(id=id)
        elif phone is not None:
            return models.User.objects.get(phone=phone)
        elif token is not None:
            return models.User.from_token(token)

        return None

    player = gh.Field(
        Player,
        id=gh.Int(description="玩家ID"),
        name=gh.String(description="玩家昵称"),
        description="获取玩家",
    )

    @staticmethod
    def resolve_player(root, info, id=None, name=None):
        if id is not None:
            return models.Player.objects.get(id=id)
        elif name is not None:
            return models.Player.objects.get(name=name)

        return None

    players = gh.List(
        gh.NonNull(Player),
        keyword=gh.String(description="关键字"),
        description="查找玩家",
    )

    @staticmethod
    def resolve_players(root, info, keyword):
        return models.Player.objects.filter(name__contains=keyword)

    token = gh.String(description="获取登录令牌")

    @staticmethod
    def resolve_token(root, info):
        req = info.context
        u = req.user
        if u.is_authenticated:
            return u.token()
        else:
            return None


class Register(gh.Mutation):
    class Arguments:
        name     = gh.String(required=True, description="昵称")
        phone    = gh.String(required=True, description="手机")
        password = gh.String(required=True, description="密码")
        smscode  = gh.Int(required=True, description="短信验证码")

    token = gh.String(required=True, description="登录令牌")
    user = gh.Field(User, required=True, description="用户")
    player = gh.Field(Player, required=True, description="玩家")

    @staticmethod
    def mutate(root, info, name, phone, password, smscode):
        if models.User.objects.filter(phone=phone).exists():
            raise GraphQLError('手机已经注册')
        elif models.Player.objects.filter(name=name).exists():
            raise GraphQLError('昵称已经注册')
        elif not utils.leancloud.verify_smscode(phone, smscode):
            raise GraphQLError('验证码不正确')

        with transaction.atomic():
            try:
                u = models.User.objects.create_user(phone=phone, password=password)
                u.save()
                p = models.Player.objects.create(user=u, name=name)
                p.save()
                c = models.Credit.objects.create(player=p)
                c.save()
            except Exception:
                import traceback
                traceback.print_exc()
                raise

        return Register(
            user=u, player=u.player,
            token=u.token(),
        )


class Login(object):
    class Arguments:
        phone    = gh.String(description="手机")
        forum_id = gh.ID(description="论坛用户ID")
        name     = gh.String(description="昵称")
        password = gh.String(required=True, description="密码")

    @classmethod
    def Field(cls, **kw):
        return gh.Boolean(
            resolver=cls.mutate,
            **props(cls.Arguments),
            **kw,
        )

    @staticmethod
    def mutate(root, info, phone=None, forum_id=None, name=None, password=None):
        if not phone:
            return None

        u = auth.authenticate(phone=phone, password=password)
        if not u:
            return None

        auth.login(info.context, u)
        return True


class Update(object):
    @classmethod
    def Field(cls, **kw):
        return gh.Field(
            Player,
            id=gh.ID(required=True, description="玩家ID"),
            bio=gh.String(description="签名"),
            resolver=cls.mutate,
            **kw,
        )

    @staticmethod
    def mutate(root, info, bio=None):
        pass


class PlayerOps(gh.ObjectType):
    login = Login.Field(description="登录")
    register = Register.Field(description="注册")
    update = Update.Field(description="更新资料")
    bind_forum = gh.Field(
        Player,
        forum_id=gh.ID(required=True, description="论坛UID"),
        forum_password=gh.String(required=True, description="论坛密码"),
        description="绑定论坛帐号",
    )
    friend = gh.Boolean(
        id=gh.ID(required=True, description="目标玩家ID"),
        description="发起好友请求",
    )
    unfriend = gh.Boolean(
        id=gh.ID(required=True, description="目标玩家ID"),
        description="移除好友/拒绝好友请求",
    )
    block = gh.Boolean(
        id=gh.ID(required=True, description="目标玩家ID"),
        description="拉黑",
    )
    unblock = gh.Boolean(
        id=gh.ID(required=True, description="目标玩家ID"),
        description="解除拉黑",
    )
