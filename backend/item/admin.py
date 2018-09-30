# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib import admin

# -- own --
from . import models


# -- code --
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'type')
    list_filter = ('type',)
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
    list_display = ('id', 'seller', 'type', 'price')
    list_filter = ()
    search_fields = ('seller__username', 'type')
    ordering = ('seller',)
