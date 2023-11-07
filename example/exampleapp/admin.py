from django.contrib import admin
from exampleapp.models import MyModel


admin.site.register(MyModel, admin.ModelAdmin)
