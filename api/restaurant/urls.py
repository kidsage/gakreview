from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.restaurant.views import NaverMapSearchView, RestaurantViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("search/", NaverMapSearchView.as_view(), name="naver_map_search"),
]
