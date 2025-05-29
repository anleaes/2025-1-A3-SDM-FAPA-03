from .models import Theater
from rest_framework import viewsets
from .serializer import TheaterSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer