from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя """

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='First Name', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Last Name', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone Number', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="Active")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['is_active', ]
