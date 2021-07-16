from django.db import models
from carts import models as carts_views

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    cart = models.ForeignKey(
        carts_views.Cart,
        on_delete=models.PROTECT,
        verbose_name="Order")
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    contact_info = models.TextField(verbose_name="Contact info")
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.contact_info

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Test(models.Model):
    cart = models.CharField(max_length=150)
    contact_info = models.TextField(verbose_name="Contact info")
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        auto_now_add=False
    )