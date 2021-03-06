from django.contrib import admin

from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "name", "price",
        "author", "publisher",
        "date"
    ]


admin.site.register(models.Book, BookAdmin)

admin.site.register(models.Author)
admin.site.register(models.Series)
admin.site.register(models.Publisher)


class PostInLine(admin.TabularInline):
    model = models.Book.genre.through


@admin.register(models.Genre)
class TagAdmin(admin.ModelAdmin):
    model = models.Genre
    inlines = [
        PostInLine,
    ]