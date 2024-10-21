from django.db import models


# Виды полей в Джанго
# CharField -> string(строка) с ограничением по длине. Длина равна max_length
# TextField -> string(строка) без ограничения по длине
# DecimalField -> Не целые числа. Кол-во цифр(всех) равна max_digits, сколько за запятой равно decimal_places
# PositiveSmallIntegerField -> Целое положительное число до 32767
# PositiveIntegerField -> Целое положительное число до 2147483647
# PositiveBigIntegerField -> Целое положительное число до 9223372036854775807

class Film(models.Model):  # Film -> имя таблицы в SQL
    # id создавать не нужно, Джанго по стандарту создает сам
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.CharField(max_length=255)
    duration = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):  # Что показывать при вызове объекта
        return self.name
