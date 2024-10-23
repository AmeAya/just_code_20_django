from django.db import models


# Виды полей в Джанго
# CharField -> string(строка) с ограничением по длине. Длина равна max_length
# TextField -> string(строка) без ограничения по длине
# DecimalField -> Не целые числа. Кол-во цифр(всех) равна max_digits, сколько за запятой равно decimal_places
# PositiveSmallIntegerField -> Целое положительное число до 32767
# PositiveIntegerField -> Целое положительное число до 2147483647
# PositiveBigIntegerField -> Целое положительное число до 9223372036854775807
# ForeignKey -> Поле, которое будет привязано к id другой таблицы

class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    # null=True -> Разрешает этому полю быть null
    # Cascade - Каскадное удаление -> При удалении записи из таблицы, все связанные записи будут удалены
    # Set NULL -> При удалении записи из таблицы, все связанные записи будут иметь NULL в этом поле

    duration = models.PositiveSmallIntegerField()
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
