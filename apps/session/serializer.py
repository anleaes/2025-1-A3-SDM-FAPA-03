from theater.serializer import TheaterSerializer
from movie.serializer import MovieSerializer
from room.serializer import RoomSerializer
from movie.models import Movie
from room.models import Room
from theater.models import Theater
from .models import Session
from rest_framework import serializers
    
class SessionSerializer(serializers.ModelSerializer):
    #receber o ID do para a criação/atualização
    #queryset valida IDs enviados e buscar objetos existentes no banco.
    theater = serializers.PrimaryKeyRelatedField(queryset=Theater.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    #somente leitura que retorna os detalhes completos
    theaterDetail = TheaterSerializer(source='theater', read_only=True)
    movieDetail = MovieSerializer(source='movie', read_only=True)
    roomDetail = RoomSerializer(source='room', read_only=True)

    class Meta:
        model = Session
        fields = ['id', 'theater', 'movie', 'room', 'price', 'language', 'theaterDetail', 'movieDetail', 'roomDetail']