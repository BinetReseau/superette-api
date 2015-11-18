from django.db import models

class Account(models.Model):
    DESCRIPTION_MAX_LENGTH = 1024
    SHORT_NAME_MAX_LENGTH = 128

    balance       = models.BigIntegerField() # Number of cents owned
    description   = models.CharField(max_length = DESCRIPTION_MAX_LENGTH)
    short_name    = models.CharField(max_length = SHORT_NAME_MAX_LENGTH)
    # TODO: owner = models.ForeignKey("LegalPerson")

    def __str__(self):
        return self.short_name
