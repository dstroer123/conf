from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя автора'
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    title = models.CharField(
        max_length=200,
        verbose_name='Название книги'
    )

    pages = models.PositiveIntegerField(
        verbose_name='Количество страниц'
    )

    def __str__(self):
        return self.title