from django.contrib import admin

# Register your models here.
from staffapp import models

admin.site.register(models.Employee)