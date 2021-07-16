from django.db import models
from django.contrib.auth import get_user_model

# from directory import models as dir_models
# from . import views
# Create your models here.

User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True,
                                 related_name="carts",
                                 verbose_name="Cart",
                                 on_delete=models.PROTECT)

    @property
    def total_price_cart(self):
        goods = self.goods.all()
        total_price = 0
        for good in goods:
            total_price += good.price
        return total_price


class BooksInCart(models.Model):
    cart = models.ForeignKey(Cart,
                             related_name="goods",
                             on_delete=models.CASCADE,
                             verbose_name="Cart")
    book = models.ForeignKey(
        'directory.Book',
        on_delete=models.PROTECT,
        verbose_name='Book',
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=5,
        decimal_places=2,
    )

    @property
    def total_price(self):
        return self.price * self.quantity
