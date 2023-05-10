from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context

# функциональная вьюха - список книг
# def list(request):
#     user = request.user.username
#     if user == 'dan':
#         books = Book.objects.all()
#         context = {'user': user, 'books': books, 'title': 'Список книг для %s' % user}
#         return render(request, template_name='lib/list.html', context=context)
#     books = Book.objects.all()
#     context = {'books': books, 'title': 'Список книг для неизвестного'}
#     return render(request, template_name='lib/list.html', context=context)

# вьюха на основе классов - список книг
class BookList(TitleMixin, ListView):
    model = Book
    template_name = 'lib/list.html'
    title = 'Список книг'

def book(request):
    book = Book.objects.get(title=str(request.path).replace('_', ' ').replace('/', '').capitalize())
    print(book)
    context = {'book': book, 'title': 'Книга %s' % book}
    return render(request, template_name='lib/book.html', context=context)