from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(verbose_name='Login', max_length=20, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=20)
    last_name = models.CharField(verbose_name='Last name', max_length=20)
    email = models.CharField(verbose_name='Email', max_length=50, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    USERNAME_FIELD = 'username'
