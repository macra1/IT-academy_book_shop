from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
# from .forms import BookForm
# from .forms import CreateBookForm
from . import forms
from directory import models
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView

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


class CreateAuthorView(DetailView):
    template_name = 'carts/cart-edit.html'
    model = models.Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateGenreView(DetailView):
    template_name = 'crud/create.html'
    model = models.Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatePublisherView(DetailView):
    template_name = 'carts/cart-edit.html'
    model = models.Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def author_create(request):
    print('author_create')
    if request.method == "POST":
        form = forms.CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse("Неверная форма")
    else:
        form = forms.CreateAuthorForm()
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def author_update(request, author_id):
    print('author_update')
    if request.method == "POST":
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse("Неверная форма")
    else:
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(instance=obj)
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def author_delete(request, author_id):
    if request.method == "POST":
        print("author_delete and metod POST")
        obj = models.Author.objects.get(pk=author_id).delete()
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'crud/book_delete.html')


def genre_create(request):
    print('genre_create')
    if request.method == "POST":
        form = forms.CreateGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse("Неверная форма")
    else:
        form = forms.CreateGenreForm()
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def genre_update(request, genre_id):
    print('genre_update')
    if request.method == "POST":
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse("Неверная форма")
    else:
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(instance=obj)
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def genre_delete(request, genre_id):
    if request.method == "POST":
        print("genre_delete and metod POST")
        obj = models.Genre.objects.get(pk=genre_id).delete()
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'crud/book_delete.html')


def publisher_create(request):
    print('publisher_create')
    if request.method == "POST":
        form = forms.CreatePublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse("Неверная форма")
    else:
        form = forms.CreatePublisherForm()
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def publisher_update(request, publisher_id):
    print('publisher_update')
    if request.method == "POST":
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponse("Неверная форма")
    else:
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(instance=obj)
    ctx = {'form': form}
    return render(request, 'crud/create.html', context=ctx)


def publisher_delete(request, publisher_id):
    if request.method == "POST":
        print("publisher_delete and metod POST")
        obj = models.Publisher.objects.get(pk=publisher_id).delete()
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'crud/book_delete.html')
