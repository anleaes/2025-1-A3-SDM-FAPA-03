from .models import Movie
from rest_framework import viewsets
from .serializer import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer  