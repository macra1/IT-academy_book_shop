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


# name = mode
# description
# price = mod
# valuta = mo
# author = mo
# genre = mod
# publisher =
# date = mode
# img = model