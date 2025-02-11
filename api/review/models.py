from django.db import models
from api.menu.models import Menu

class Review(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.menu.name}"