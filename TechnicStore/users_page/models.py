from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Class for describing a model with a user"""

    phone = PhoneNumberField(null=False, blank=False,
                             unique=False, verbose_name='Телефон')
    basket = models.ManyToManyField(
        'catalog.Products', related_name='bin', verbose_name='Кошик')
    like = models.ManyToManyField(
        'catalog.Products', related_name='like', verbose_name='Товари що сподобалися')
    comparison = models.ManyToManyField(
        'catalog.Products', related_name='comparison', verbose_name='Товари для порівняня')

    class Meta:
        db_table = 'user'
        verbose_name = 'Користувачі'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return f'{self.first_name}'
