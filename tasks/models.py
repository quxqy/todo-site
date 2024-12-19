from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(unique=True,null=False, max_length=128)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        return self.completed

from django.contrib.auth.models import AbstractUser
from django.db import models

