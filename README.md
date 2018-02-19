### django-hidefield ###

Provides a field base class to hide fields in django admin.
The class turns a field label in an admin edit form into a
show/hide toggle link.

Tested with Django 1.11.

#### Installation ####

- `pip install django-hidefield`
- place `'hidefield'` in `INSTALLED_APPS`

#### Usage ####

Build a custom field class for any model field type you want to hide.
The field has an additional argument `hide` with the following meaning:

- `'closed'`    : default, the field is hidden at start
- `'data'`      : the field is hidden at start, if the field contains data
- `'no-data'`   : the field is hidden at start, if the field contains no data
- `'opened'`    : (or any other value) the field is shown at start

#### Example ####

```python
from django.db import models
from hidefield.fields import HideField


class HideCharField(HideField, models.CharField):
    pass


class MyModel(models.Model):
    name = HideCharField(max_length=32, hide='data')
```

See `exampleapp` for more examples.