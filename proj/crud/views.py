from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
# from .forms import BookForm
# from .forms import CreateBookForm
from . import forms
from directory import models
from django.urls import reverse
from django.views.generic import ListView

# Create your views here.


def create(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = "Неверная форма"

    form = BookForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'crud/create.html', data)


def read(request, page=0):
    data, books = None, None
    if page == 0:
        data = models.Book.objects.all()
        # return render(request, 'crud/read.html', {"data": data})
    else:
        books = models.Book.objects.filter(pk=page)
        # return render(request, 'crud/read.html', {'books': books})
    return render(request, 'crud/read.html', {"data": data, 'books': books})


def univread(request, modeltype):
    author, genre, publisher, books = None, None, None, None
    if modeltype == "author":
        print("author")
        author = models.Author.objects.all()
    elif modeltype == "book":
        print("бук")
        books = models.Book.objects.all()
    elif modeltype == "genre":
        print("genre")
        genre = models.Genre.objects.all()
    elif modeltype == "publisher":
        print("publisher")
        publisher = models.Publisher.objects.all()
    else:
        return HttpResponse("Errorrr")
    return render(request, 'crud/read.html', {'books': books,
                                              "Author": author,
                                              "Genre": genre,
                                              "Publisher": publisher})


def univread_detail(request, modeltype, page=1):
    author, genre, publisher, books = None, None, None, None
    if modeltype == "author":
        print("автор")
        author = models.Author.objects.filter(pk=page)
    elif modeltype == "book":
        print("book")
        books = models.Book.objects.filter(pk=page)
    elif modeltype == "genre":
        genre = models.Genre.objects.filter(pk=page)
    elif modeltype == "publisher":
        publisher = models.Publisher.objects.filter(pk=page)
    else:
        return HttpResponse("Errorrr")
    return render(request, 'crud/detailview.html', {'books': books,
                                                    "Author": author,
                                                    "Genre": genre,
                                                    "Publisher": publisher})


def book_create(request):
    print('book_create')
    if request.method == "POST":
        form = forms.CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books'))
        else:
            return HttpResponse("Неверная форма")
    else:
        form = forms.CreateBookForm()
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def book_update(request, book_id):
    print('book_update')
    if request.method == "POST":
        obj = models.Book.objects.get(pk=book_id)
        form = forms.CreateBookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books'))
        else:
            return HttpResponse("Неверная форма")
    else:
        obj = models.Book.objects.get(pk=book_id)
        form = forms.CreateBookForm(instance=obj)
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def book_delete(request, book_id):
    if request.method == "POST":
        print("book_delete and metod POST")
        obj = models.Book.objects.get(pk=book_id).delete()
        return HttpResponseRedirect(reverse('books'))
    return render(request, 'crud/book_delete.html')


class BookListView(ListView):
    model = models.Book
    print(model)