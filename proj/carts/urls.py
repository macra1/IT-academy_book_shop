from django.urls import path
from . import views

urlpatterns = [
    # path('?book_id=<int:book_id>', views.CartView.as_view(), name='cart-edit'),
    path('update_cart/', views.CartUpdate.as_view(), name='cart-update'),
    path('delete-good-in-cart/<int:pk>', views.DeleteGoodInCartView.as_view(), name='delete-good-in-cart'),
    path('', views.CartView.as_view(), name='cart-edit'),
]
