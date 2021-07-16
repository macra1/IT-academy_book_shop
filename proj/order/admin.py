from django.contrib import admin
from . import models
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "pk", "status",
        "contact_info", "created",
        "updated"
    ]


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Status)
