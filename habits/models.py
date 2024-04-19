# Create your models here.
from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class NiceHabit(models.Model):
    """Модель хорошей привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=50, **NULLABLE, verbose_name='Место')
    action = models.CharField(max_length=50, verbose_name='Действие')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Хорошая привычка'
        verbose_name_plural = 'Хорошие привычки'


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    time = models.TimeField(verbose_name='Время привычки')
    place = models.CharField(max_length=50, verbose_name='Место')
    action = models.CharField(max_length=50, verbose_name='Действи')
    reward = models.CharField(max_length=50, **NULLABLE, verbose_name='Награда')
    associated_nice_habit = models.ForeignKey(NiceHabit, on_delete=models.SET_NULL,
                                              **NULLABLE, verbose_name='Сопутствующая приятная привычка')
    periodicity = models.PositiveIntegerField(verbose_name='Периодичность')
    is_public = models.BooleanField(default=False, verbose_name='Является общедоступным')
    duration_time = models.TimeField(verbose_name='Продолжительность')
    next_date = models.DateField(**NULLABLE, verbose_name="Дата следующего действия по привычке")

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
