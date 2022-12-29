from django.contrib import admin

# Register your models here.
from sreeapp import models

admin.site.register(models.Todo)
