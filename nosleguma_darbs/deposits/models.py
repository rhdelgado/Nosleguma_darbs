from django.db import models
from django.urls import reverse


class Deposit(models.Model):

    deposit = models.IntegerField(max_length=5)
    term = models.DecimalField(decimal_places=0, max_digits=1)
    rate = models.DecimalField(decimal_places=3, max_digits=3)


    def __str__(self):
        return self.deposit


    def get_absolute_url(self):
        return f"/deposits/<int:pk>/"




