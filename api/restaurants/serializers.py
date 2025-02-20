from rest_framework import serializers

from ..menus.models import Menu
from ..menus.serializers import MenuSerializer
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ["id", "name", "lat", "lng", "menus"]
