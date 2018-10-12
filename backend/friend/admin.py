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
    list_display = ('id', 'player', 'friend', 'created')
    list_filter = ()
    search_fields = ('player__name',)
    ordering = ('id',)


@admin.register(models.Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'block', 'created')
    list_filter = ()
    search_fields = ('player__name',)
    ordering = ('id',)
