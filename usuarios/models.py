from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class UserRoles(models.TextChoices):
    ADMIN = 'ADM', 'Administrador'
    LOJA = 'LOJA', 'Loja'


class Usuario(AbstractUser):
    role = models.CharField(default=UserRoles.LOJA,choices=UserRoles.choices)

    def save(self, *args, **kwargs):
        if self.role == UserRoles.ADMIN:
            self.is_staff = True
        return super().save(*args, **kwargs)