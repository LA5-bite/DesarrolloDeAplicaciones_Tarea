from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = "GESTOR", "Gestor"
        USER = "USUARIO", "Usuario"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        verbose_name="rol",
    )

    @property
    def display_role(self):
        if self.is_superuser or self.is_staff:
            return "Administrador"
        return self.get_role_display()
