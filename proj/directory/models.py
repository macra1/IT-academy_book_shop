from django.db import models
from datetime import date


class Author(models.Model):
    name = models.CharField(verbose_name="Имя автора", max_length=100, default="Неизвестный автор")
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    name = models.CharField(verbose_name="Имя жанра", max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Publisher(models.Model):
    name = models.CharField(verbose_name="Название издательства", max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Book(models.Model):
    name = models.CharField(verbose_name="Название книги", max_length=100)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name="Жанры", blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(verbose_name="Дата публикации", default=date.today)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Series(models.Model):
    name = models.CharField(verbose_name="Серия книг", max_length=100)
    description = models.TextField(blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"
