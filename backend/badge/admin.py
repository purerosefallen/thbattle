# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib import admin

# -- own --
from . import models


# -- code --
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
