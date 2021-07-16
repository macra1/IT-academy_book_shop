from django.contrib import admin
from . import models

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['pk']


class BookInCartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cart', 'book', 'quantity', 'price']


admin.site.register(models.BooksInCart, BookInCartAdmin)
admin.site.register(models.Cart, CartAdmin)
