from django.contrib import admin
from . import models

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ["pk"]


admin.site.register(models.Cart, CartAdmin)
