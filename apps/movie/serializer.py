from .models import Movie
from gender.models import Gender
from gender.serializer import GenderSerializer
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    #retorna os gêneros como objetos detalhados (via GenderSerializer)
    gender = GenderSerializer(many=True, read_only=True)
    
    #permite enviar uma lista de IDs para associar gêneros ao filme
    genderIds = serializers.PrimaryKeyRelatedField(
        many=True,                        # permite múltiplos IDs
        queryset=Gender.objects.all(),   # define quais IDs são válidos
        write_only=True,                 # campo só aparece na escrita (POST/PUT), não na resposta
        source='gender'                  # os dados vão ser salvos na campo gender do model
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'description', 'poster', 'gender', 'genderIds']