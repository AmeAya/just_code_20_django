from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Вью -> Класс/функция которая "готовит" данные из моделек и выгружает их
# Генерики - Django Generic Views -> Вью, встроенные в Джанго
# Генерики:
# ListView -> Генерик, который вытаскивает все записи из модели(SELECT ALL)


class GenreListView(ListView):
    model = Genre  # С какой модели брать данные
    context_object_name = 'genre_list'  # Как назвать эти данные
    template_name = 'genre_list.html'  # Имя html темплейта, куда пойдут данные
