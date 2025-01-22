from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(unique=True,null=False, max_length=128)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Задача: {self.name} | Статус {self.completed} | Пользователь {self.user}"



