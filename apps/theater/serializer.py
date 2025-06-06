from .models import Theater
from rest_framework import serializers

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ['id', 'name', 'openingHours', 'address', 'contactNumber']