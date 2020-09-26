from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Contactus)
class ContactDetails(admin.ModelAdmin):
    list_display = ['fullname', 'description', 'date']