from rest_framework import viewsets
from api.menu.models import Menu
from api.menu.serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer