from django.contrib import admin

class SecureFileAdmin(admin.ModelAdmin):
    filter_horizontal = ("shared_with",)

# Register your models here.
from .models import  SecureFile

admin.site.register(SecureFile, SecureFileAdmin),