from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=12, null=True);
    room = models.CharField(max_length=10, null=True);
