from rest_framework import serializers
from api.menu.models import Menu
from api.review.serializers import ReviewSerializer

class MenuSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'