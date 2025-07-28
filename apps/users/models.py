from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    email = models.EmailField(
        ('Email'),
        unique=True,
    )
    phone_number = PhoneNumberField(
        ('Номер телефона'),
        help_text=('Пример: +996500123456'),
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
