from django.db import models

from ..restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
