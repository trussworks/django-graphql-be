from django.contrib import admin

from . import models

# Registers the models that can be updated using the admin interface:
admin.site.register(models.Person)
admin.site.register(models.Case)
