from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class UserTypeChoices(models.TextChoices):
        COMUM = 'comum', 'Comum'
        LOJISTA = 'lojista', 'Lojista'

    cpf = models.CharField(max_length=11)
    user_type = models.CharField('Tipo de usuário', max_length=10, choices=UserTypeChoices, default=UserTypeChoices.COMUM)
