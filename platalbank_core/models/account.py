from django.db import models

class Account(models.Model):
    balance = models.IntegerField() # Number of cents owned
    description = models.CharField(max_length=1024)
    short_name = models.CharField(max_length=128)
    # TODO: owner = models.ForeignKey("LegalPerson")

    def __str__(self):
        return self.short_name
