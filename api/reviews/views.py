from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        menu_id = self.kwargs["menu_id"]
        return Review.objects.filter(menu_id=menu_id)

    def perform_create(self, serializer):
        menu_id = self.kwargs["menu_id"]
        serializer.save(menu_id=menu_id)
