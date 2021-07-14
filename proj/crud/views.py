from django.shortcuts import render, redirect, HttpResponse
from .forms import BookForm
from directory import models

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