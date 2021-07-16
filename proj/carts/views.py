from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, DeleteView
from . import models
from directory import models as dir_mod
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


# def get_price(item):
#     obj = dir_mod.Book.objects.filter(pk=item)
#     print(obj.pk)
#     return obj.pk


class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')
        if action == "save_cart":
            cart_id = self.request.session.get('cart_id')
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={},
            )
            if created:
                self.request.session['cart_id'] = cart.pk
            goods = cart.goods.all()
            if goods:
                for key, value in request.POST.items():
                    if "quantityforgood_" in key:
                        print(key, value)
                        pk = int(key.split('_')[1])
                        good = goods.get(pk=pk)
                        good.quantity = int(value)
                        good.save()
            return HttpResponseRedirect(reverse_lazy("cart-edit"))
        elif action == "create_order":
            return HttpResponseRedirect(reverse_lazy('create-order'))
        else:
            return HttpResponseRedirect(reverse_lazy("cart-edit"))


class CartView(DetailView):
    template_name = 'carts/cart-edit.html'
    model = models.Cart

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        book_id = self.request.GET.get('book_id')
        if book_id:
            book = dir_mod.Book.objects.get(pk=int(book_id))
            book_in_cart, flat_created = models.BooksInCart.objects.update_or_create(
                cart=cart,
                book=book,
                defaults={
                    'price': book.price
                }
            )
            if not flat_created:
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.price = book_in_cart.book.price * q
            else:
                book_in_cart.price = book.price

            book_in_cart.save()
        return cart


class DeleteGoodInCartView(DeleteView):
    model = models.BooksInCart
    success_url = reverse_lazy("cart-edit")
