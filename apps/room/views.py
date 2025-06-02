from .models import Room
from rest_framework import viewsets
from .serializer import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer  