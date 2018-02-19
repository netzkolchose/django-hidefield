# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.fields import Field
from django.forms.widgets import Widget

# cache for created widget classes
widget_classes = {}


def widget_factory(cls):
    return widget_classes.setdefault(
        cls, type(str('Hide_%s' % cls.__name__), (HideWidget, cls), {}))


class HideWidget(Widget):
    template_name = 'hidefield/hidefield.html'
    hide = 'closed'

    class Media:
        js = ('hidefield/hidefield.js',)

    def get_context(self, name, value, attrs):
        collapsed = 'false'
        if self.hide == 'closed':
            collapsed = 'true'
        elif self.hide == 'no-data' and not value:
            collapsed = 'true'
        elif self.hide == 'data' and value:
            collapsed = 'true'
        ctx = super(HideWidget, self).get_context(name, value, attrs)
        ctx['widget']['collapsed'] = collapsed
        ctx['widget']['super_template'] = super(HideWidget, self).template_name
        return ctx


class HideField(Field):
    def __init__(self, *args, **kwargs):
        self.hide = kwargs.pop('hide', 'closed')
        super(HideField, self).__init__(*args, **kwargs)

    def formfield(self, form_class=None, choices_form_class=None, **kwargs):
        key = kwargs.get('widget')
        if not key:
            field = super(HideField, self).formfield(**kwargs)
            key = field.widget.__class__
        kwargs['widget'] = widget_factory(key)
        field = super(HideField, self).formfield(**kwargs)
        field.widget.hide = self.hide
        return field
