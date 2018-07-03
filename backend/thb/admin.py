# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

# -- own --
from . import models

# -- code --
# Register your models here.
admin.site.site_header = '东方符斗祭后台'


@admin.register(models.User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', ('phone', 'verified'))}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'id', 'email', 'phone', 'verified', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'verified', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone')
    ordering = ('username',)


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'ppoint', 'jiecao', 'games', 'drops')
    list_filter = ()
    search_fields = ('user__username', 'user__phone', 'user__email')
    ordering = ('user',)


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'type', 'arg', 'status')
    list_filter = ('type', 'status')
    search_fields = ('owner__username',)
    ordering = ('owner',)


@admin.register(models.ItemActivity)
class ItemActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'item', 'extra', 'created')
    list_filter = ('action',)
    search_fields = ('user__username', 'item__type')
    ordering = ('user',)


@admin.register(models.Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'item', 'price')
    list_filter = ()
    search_fields = ('seller__username', 'item__type')
    ordering = ('seller',)


@admin.register(models.Unlocked)
class UnlockedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item')
    list_filter = ()
    search_fields = ('user__username', 'item')
    ordering = ('user',)


@admin.register(models.Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'achievement')
    list_filter = ()
    search_fields = ('user__username', 'achievement')
    ordering = ('user',)


@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'testing')
    list_filter = ()
    search_fields = ()
    ordering = ('id',)


@admin.register(models.BadgeType)
class BadgeTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'icon2x', 'description')
    list_filter = ()
    search_fields = ('title', 'description')
    ordering = ('title',)


@admin.register(models.Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'type', 'created')
    list_filter = ('type',)
    search_fields = ('owner__username', 'type__title', 'type__description')
    ordering = ('id',)


@admin.register(models.Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'friend', 'created')
    list_filter = ()
    search_fields = ('user__username',)
    ordering = ('id',)


@admin.register(models.Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'block', 'created')
    list_filter = ()
    search_fields = ('user__username',)
    ordering = ('id',)


@admin.register(models.Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'founder', 'president', 'slogan', 'totem', 'created')
    list_filter = ()
    search_fields = ('name', 'founder__username', 'president__username')
    ordering = ('id',)


@admin.register(models.GuildMember)
class GuildMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'guild', 'member', 'joined')
    list_filter = ()
    search_fields = ('guild__name', 'member__username')
    ordering = ('id',)


@admin.register(models.GuildBadge)
class GuildBadgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'guild', 'type', 'created')
    list_filter = ()
    search_fields = ('guild__name', 'type__title')
    ordering = ('id',)


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ()
    search_fields = ('text',)
    ordering = ('id',)
