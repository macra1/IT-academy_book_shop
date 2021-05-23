from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name="Автор",max_length=100)
    description = models.TextField()


class Series(models.Model):
    name = models.CharField(verbose_name="Серия книг", max_length=100)


class Genre(models.Model):
    name = models.CharField(verbose_name="Жанр", max_length=50)
    description = models.TextField()


class Publisher(models.Model):
    name = models.CharField(verbose_name="Издательство", max_length=100)
    description = models.TextField()
