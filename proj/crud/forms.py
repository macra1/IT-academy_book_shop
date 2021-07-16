from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select, SelectMultiple, ImageField
from directory.models import Book, Author, Genre, Publisher


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Книги'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание Книги'
            }),
        }


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'author', 'genre', 'publisher', 'img']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Книги'}),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание Книги'}),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена за 1 шт.'}),
            "author": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автор книги'}),
            "genre": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр'}),
            "publisher": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Издательство'}),
        }


class CreateAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'description']
        widgets = {"name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название '}),
            "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание '})}


class CreateGenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
        widgets = {"name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название '}),
            "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание '})}


class CreatePublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description']
        widgets = {"name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название '}),
            "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание '})}
