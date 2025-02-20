from django.db import models

from ..menus.models import Menu


class Review(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.menu.name}"
