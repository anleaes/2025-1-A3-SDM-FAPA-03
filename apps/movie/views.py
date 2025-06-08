from .models import Movie
from rest_framework import viewsets
from .serializer import MovieSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer  
    parser_classes = [MultiPartParser, FormParser]