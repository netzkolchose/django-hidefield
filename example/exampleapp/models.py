# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from hidefield.fields import HideField
from django.utils.encoding import python_2_unicode_compatible


class HideCharField(HideField, models.CharField):
    pass


class HideTextField(HideField, models.TextField):
    pass


class HideForeignKey(HideField, models.ForeignKey):
    pass


@python_2_unicode_compatible
class MyModel(models.Model):
    name = HideCharField(max_length=32)
    text = HideTextField(hide='no-data')
    parent = HideForeignKey('self', blank=True, null=True, hide='data')

    def __str__(self):
        return self.name
