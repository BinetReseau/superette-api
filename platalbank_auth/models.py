#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

class User(AbstractUser):
    phone_number = models.CharField(
            max_length=14,
            validators=[
                validators.RegexValidator(r'^\d\d-$\d\d-$\d\d-$\d\d-$\d\d$',
                    'Enter a valid phone number : format : 06-66-66-66-66',
                    'invalid')
                ]
            )

    room = models.CharField(max_length=128)
