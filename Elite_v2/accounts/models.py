from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    imgProfil = models.ImageField(upload_to='imgProfil/', blank=True, null=True, verbose_name="Photo de profil")

