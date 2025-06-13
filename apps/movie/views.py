from .models import Movie
from rest_framework import viewsets
from .serializer import MovieSerializer
from rest_framework.parsers import MultiPartParser

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer  

    # definindo um parser que interpreta os dados recebidos nas requisições
    # MultiPartParser: Lê requisições com multipart/form-data 
    #multipart/form-data é o tipo de conteúdo usado quando um formulário envia arquivos + dados juntos).
    parser_classes = [MultiPartParser]