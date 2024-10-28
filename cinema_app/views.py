from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Вью -> Класс/функция которая "готовит" данные из моделек и выгружает их
# Генерики - Django Generic Views -> Вью, встроенные в Джанго
# Генерики:
# ListView -> Генерик, который вытаскивает все записи из модели(SELECT ALL)
# DetailView -> Генерик, который вытаскивает только одну запись по id(SELECT * FROM ... WHERE id=)
# CreateView -> Генерик, который создает форму для ввода данных чтобы создать запись


class GenreListView(ListView):
    model = Genre  # С какой модели брать данные
    context_object_name = 'genre_list'  # Как назвать эти данные
    template_name = 'genre_list.html'  # Имя html темплейта, куда пойдут данные


from django.views.generic import DetailView


class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'genre_detail.html'


from django.views.generic import CreateView


class GenreCreateView(CreateView):
    model = Genre
    template_name = 'genre_create.html'
    # fields = ['name']
    fields = '__all__'  # Все поля
    success_url = 'genres'  # Куда перекинуть после создания
