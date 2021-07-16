from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('t3', views.t3),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<some_txt>', views.http),
]
