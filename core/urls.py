"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cinema_app.views import *  # Импортируем все вью из views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres', GenreListView.as_view(), name='genres_url'),  # Добавляем новый маршрут к GenreListView
    # path('<URL в адресной строке>', <Вью, к которой должен идти маршрут>)

    path('genre/<int:pk>',  GenreDetailView.as_view(), name='genre_detail_url'),
    # <int:pk> -> Integer, который пойдет во вью как pk(Primary Key). Одно и то же что и id
    # 127.0.0.1:8000/genre/1 -> pk=1
    # 127.0.0.1:8000/genre/5 -> pk=5

    # name -> Имя маршрута внутри Джанго
    path('genre_create', GenreCreateView.as_view()),
    path('genre_update/<int:pk>', GenreUpdateView.as_view()),  # 127.0.0.1:8000/genre_update/3 -> pk=3
    path('genre_delete/<int:pk>', GenreDeleteView.as_view()),
    path('about_us', AboutUsTemplateView.as_view()),
]
