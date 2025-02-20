from django.urls import path

from .views import MenuDetailView, MenuListCreateView

urlpatterns = [
    path("", MenuListCreateView.as_view(), name="menu-list-create"),
    path("<int:pk>/", MenuDetailView.as_view(), name="menu-detail"),
]
