from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name="Автор", max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Valuta(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name="Жанр", max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(verbose_name="Издательство", max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(verbose_name="Название книги", max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    valuta = models.ForeignKey(Valuta, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(verbose_name="Серия книг", max_length=100)
    description = models.TextField(blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
