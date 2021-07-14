from django.urls import path
from .views import http, t3


urlpatterns = [
    path('t3', t3),
    path('<some_txt>', http),
]