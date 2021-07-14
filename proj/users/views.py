from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def http(request, some_txt):
    return HttpResponse(f"some test http and {some_txt}")


def t3(request):
    return render(request, "ТЗ на создание сайта.htm")
