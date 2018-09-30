# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# -- stdlib --
# -- third party --
from django.contrib import admin

# -- own --
from . import models


# -- code --
# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'title', 'ppoint', 'jiecao', 'games', 'drops')
    list_filter = ()
    search_fields = ('user__username', 'phone', 'user__email')
    ordering = ('user',)
