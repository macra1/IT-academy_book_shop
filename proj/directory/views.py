from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def home(request):
    answer = ""
    post = Book.objects.all()
    for i in post:
        answer += str(i)
        answer += " <p> "
    return HttpResponse(answer)


def test(request):
    return render(request, "New_form.html")


def test2(request):
    return render(request, "Base.html")


def bok(request, bok):
    return HttpResponse(bok)


def main(request):
    return render(request, "directory/Main.html")


def show_books(request):
    answer = Book.objects.order_by("name")
    return render(request, "New_form.html", {"books": answer})
