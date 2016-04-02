from django.db import models

class FrankizUser(models.Model):
    hruid = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256);
    last_name = models.CharField(max_length=256);
    email = models.EmailField();
    phone = models.CharField(max_length=12, null=True);
    room = models.CharField(max_length=10, null=True);

    def __str__(self):
        return self.first_name + " " + self.last_name
