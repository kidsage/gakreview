from rest_framework import serializers
from api.restaurant.models import Restaurant
from api.menu.serializers import MenuSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'