from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SEX_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    sex = models.CharField('Пол', choices=SEX_CHOICES, max_length=10, blank=True)
    date_of_birth = models.DateField('Дата рождения')
    photo = models.ImageField('Фото', upload_to='users/', blank=True)
