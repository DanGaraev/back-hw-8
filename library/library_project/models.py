from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    cover = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Обложка')
    is_published = models.BooleanField(default=True, verbose_name='Выпущена')
    genre = models.ManyToManyField('Genre', null=True, verbose_name='Жанр')
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']


class Genre(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование жанра')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']


class Author(models.Model):
    title = models.CharField(max_length=150, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['title']