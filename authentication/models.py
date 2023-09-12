from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import UserManager

# Create your models here.


class User(AbstractUser):
    TYPE_CHOICES = (
        ("SELLER", "SELLER"),
        ("BUYER", "BUYER"),
    )
    username = None
    email = models.EmailField(unique=True)
    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        default="SELLER"
        )
    profile_image = models.ImageField(
        upload_to='authentication/images',
        blank=True,
        null=True
        )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
