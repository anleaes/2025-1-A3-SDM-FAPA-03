from .models import Movie
from gender.models import Gender
from gender.serializer import GenderSerializer
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(many=True, read_only=True)
    genderIds = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Gender.objects.all(), write_only=True, source='gender'
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'description', 'poster', 'gender', 'genderIds']