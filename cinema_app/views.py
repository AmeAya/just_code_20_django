from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Вью -> Класс/функция которая "готовит" данные из моделек и выгружает их
# Генерики - Django Generic Views -> Вью, встроенные в Джанго
# Генерики:
# ListView -> Генерик, который вытаскивает все записи из модели(SELECT ALL)
# DetailView -> Генерик, который вытаскивает только одну запись по id(SELECT * FROM ... WHERE id=)
# CreateView -> Генерик, который создает форму для ввода данных, чтобы создать запись
# UpdateView -> Генерик, который создает форму для ввода данных чтобы обновлить уже существующую запись
# DeleteView -> Генерик, который по POST запросу удаляет запись
# TemplateView -> Генерик, который возвращает html страницу


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


from django.views.generic import UpdateView
from django.urls import reverse_lazy


class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'genre_update.html'
    fields = '__all__'
    success_url = reverse_lazy('genres_url')
    # reverse -> Перенаправление по name в urls
    # reverse_lazy -> Тот же reverse, но ждет пока все процессы закончатся


from django.views.generic import DeleteView


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'genre_delete.html'
    context_object_name = 'Genre'
    success_url = reverse_lazy('genres_url')


from django.views.generic import TemplateView


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'


# создать CountryUpdateView и CountryDeleteView


# 1) Создать новый Джанго проект(Установить Джанго, создать "ядро", создать папку для темплейтов и в сеттингах указать
#    ее(TEMPLATES -> 'DIRS': [BASE_DIR / 'templates'],
# 2) Создать новый application -> library_app, добавить его в сеттингах(INSTALLED_APPS)
# 3) Создать новые модельки для library_app(Book, Author). У модельки Book должен быть ForeignKey к Author
# 4) Создать для книг ListView, DetailView, CreateView, DeleteView, UpdateView(Включая url и темплейты)


def film_list_view(request):
    # request -> Запрос, который приходит по url во view

    # films = Film.objects.all()  # QuerySet всех фильмов
    # # <МОДЕЛЬКА>.objects.all() ->  Получить все записи из <МОДЕЛЬКА>

    # films = Film.objects.filter(rating__gt=5)
    # # QuerySet фильмов с рейтингом больше 5
    #
    # # <МОДЕЛЬКА>.objects.filter(<УСЛОВИЕ>) ->  Получить все записи из
    # #                     <МОДЕЛЬКА>, у которых <УСЛОВИЕ> выполняется
    # # __gt -> Greater Than -> Больше чем (>)
    # # __lt -> Less Than -> Меньше чем (<)
    # # __gte -> Greater Than or Equal -> Больше чем или равно (>=)
    # # __lte -> Less Than or Equal -> Меньше чем или равно (<=)

    # films = Film.objects.get(id=0)
    # # <МОДЕЛЬКА>.objects.get(<УСЛОВИЕ>) -> Получить только одну записи из
    # #                        <МОДЕЛЬКА>, у которых <УСЛОВИЕ> выполняется
    # # Если по <УСЛОВИЕ> найдется больше чем 1 запись -> ОШИБКА!
    # # Если по <УСЛОВИЕ> найдется меньше чем 1 запись -> ОШИБКА!

    genre_thriller = Genre.objects.get(name='Thriller')
    films = Film.objects.filter(genre=genre_thriller)

    context = {
        'film_list': films,
        'abc': 'Hello, world!',
        'qwe': 125
    }  # context -> dict, который приходит на темплейт
    # render -> Функция Джанго, которая "рисует" темплейт с данными context
    return render(request, 'film_list.html', context=context)


def film_detail_view(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
        context = {
            'film': film
        }
    except Film.DoesNotExist:
        # В любой модели Джанго есть ошибка DoesNotExist
        context = {}
    return render(request, 'film_detail.html', context=context)


def film_create_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        countries = Country.objects.all()
        context = {
            'genres': genres,
            'countries': countries
        }
        return render(request, 'film_create.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('film_name')
        description = request.POST.get('film_description')
        rating = request.POST.get('film_rating')
        genre_id = request.POST.get('film_genre')
        duration = request.POST.get('film_duration')
        country_id = request.POST.get('film_country')

        genre = Genre.objects.get(id=genre_id)  # Находим этот жанр по айди
        country = Country.objects.get(id=country_id)  # Находим эту страну по айди
        # Чтобы заполнить Foreign Key нужно запихивать не айди,
        # нужно вытащить его из базы запросом

        film = Film(
            name=name,
            description=description,
            rating=rating,
            genre=genre,
            duration=duration,
            country=country
        )  # Создаем новый объект модели Film
        film.save()  # Сохраняем этот объект как запись в SQL

        from django.shortcuts import redirect
        return redirect(film_list_view)
