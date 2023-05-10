from django.contrib import admin

from .models import Book, Genre, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'genre')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
