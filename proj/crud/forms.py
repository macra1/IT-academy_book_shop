from django.forms import ModelForm, TextInput, Textarea
from directory.models import Book


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
        fields = ['name', 'description']

        widgets = {
            "name": TextInput(attrs={'placeholder': 'Название Книги'}),
            "description": Textarea(attrs={'placeholder': 'Описание Книги'}),
        }


# name
# description
# price
# valuta
# author
# genre
# publisher
# date
# img