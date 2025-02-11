from rest_framework import viewsets
from api.restaurant.models import Restaurant
from api.restaurant.serializers import RestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer