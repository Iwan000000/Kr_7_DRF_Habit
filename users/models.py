# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель для пользователей"""
    username = None
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    telegram_chat_id = models.CharField(max_length=50, verbose_name='Telegram chat ID')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='Аватар')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
