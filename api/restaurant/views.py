import requests
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.restaurant.models import Restaurant
from api.restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class NaverMapSearchView(APIView):
    def get(self, request):
        query = request.GET.get("query", "음식점")
        url = "https://openapi.naver.com/v1/search/local.json"
        headers = {
            "X-Naver-Client-Id": settings.NAVER_CLIENT_ID,
            "X-Naver-Client-Secret": settings.NAVER_CLIENT_SECRET,
        }
        params = {"query": query, "display": 5}

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response(
                {"error": "Failed to fetch data from Naver API"},
                status=status.HTTP_400_BAD_REQUEST,
            )
