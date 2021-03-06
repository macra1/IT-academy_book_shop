from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import UpdateView, DetailView, DeleteView, FormView
from . import forms, models
from carts import models as carts_models
from django.urls import reverse_lazy

# Create your views here.


class CreateOrderView(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'order/create-order.html'
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = carts_models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            return HttpResponseRedirect(reverse_lazy('cart-edit'))
        ci = form.cleaned_data.get('contact_info')
        st = models.Status.objects.get(pk=1)
        order = models.Order.objects.update_or_create(
            cart=cart,
            contact_info=ci,
            status=st,
        )
        self.request.session.delete('cart_id')
        if self.request.user.is_authenticated:
            cart_id = self.request.session.get('cart_id')
            customer1 = carts_models.Cart.objects.get(pk=cart_id)
            customer1.customer = self.request.user
            customer1.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = carts_models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        context['object'] = cart
        return context


def success(requsest):
    return render(requsest, 'order/success.html')