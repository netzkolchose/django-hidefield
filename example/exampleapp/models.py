from django.db import models
from hidefield.fields import HideField



class HideCharField(HideField, models.CharField):
    pass
class HideTextField(HideField, models.TextField):
    pass
class HideForeignKey(HideField, models.ForeignKey):
    pass


class MyModel(models.Model):
    name = HideCharField(max_length=32)
    text = HideTextField(hide='no-data')
    parent = HideForeignKey('self', blank=True, null=True, hide='data', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
