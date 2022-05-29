from django.db import models

# Create your models here.
from users.models import User


class Project(models.Model):
    name = models.CharField(verbose_name="Название проекта", max_length=40, unique=True)
    repository_url = models.URLField(verbose_name="Репозиторий", max_length=200)
    users = models.ManyToManyField(User, verbose_name="Пользователи")

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT)
    is_active = models.BooleanField(blank=True)
