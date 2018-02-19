# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from exampleapp.models import MyModel


admin.site.register(MyModel, admin.ModelAdmin)

