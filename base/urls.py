from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/restaurants/", include("api.restaurants.urls")),
    path("api/menus/", include("api.menus.urls")),
    path("api/reviews/", include("api.reviews.urls")),
]
