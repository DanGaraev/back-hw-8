from django.urls import path, include

from .views import *

app_name = 'library_project'

urlpatterns = [
    # для функ. вьюхи
    # path('', list, name='list'),
    # для клас. вьюхи
    path('', BookList.as_view(), name='list'),
    path('ya_ne_znayu_kak_nazvat/', book)
]