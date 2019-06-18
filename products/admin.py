from django.contrib import admin
from .models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display =("name","price")


admin.site.register(Products,ProductAdmin)
