from rest_framework import serializers

from ..reviews.serializers import ReviewSerializer
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "name", "price", "reviews"]
