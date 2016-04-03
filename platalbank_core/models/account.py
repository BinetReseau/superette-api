from django.db import models
from django.conf import settings

class Account(models.Model):
    DESCRIPTION_MAX_LENGTH = 1024
    SHORT_NAME_MAX_LENGTH = 128

    balance       = models.BigIntegerField() # Number of cents owned
    description   = models.CharField(max_length = DESCRIPTION_MAX_LENGTH)
    short_name    = models.CharField(max_length = SHORT_NAME_MAX_LENGTH)
    owner        = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="account", default=1)
    # TODO: owner = models.ForeignKey("LegalPerson")

    def __str__(self):
        return self.short_name
