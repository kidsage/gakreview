from django.urls import path

from .views import ReviewListCreateView

urlpatterns = [
    path(
        "menus/<int:menu_id>/reviews/",
        ReviewListCreateView.as_view(),
        name="review-list-create",
    ),
]
