# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib import admin

# -- own --
from . import models


# -- code --
@admin.register(models.Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'founder', 'leader', 'slogan', 'totem', 'founded')
    list_filter = ()
    search_fields = ('name', 'founder__username', 'leader__username')
    ordering = ('id',)


@admin.register(models.GuildMember)
class GuildMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'guild', 'user', 'joined')
    list_filter = ()
    search_fields = ('guild__name', 'user__username')
    ordering = ('id',)
