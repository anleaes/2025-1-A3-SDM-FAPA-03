from .models import Session
from rest_framework import serializers
    
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'