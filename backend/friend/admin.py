# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib import admin

# -- own --
from . import models


# -- code --
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
