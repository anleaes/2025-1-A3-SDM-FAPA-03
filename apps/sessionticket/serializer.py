from .models import SessionTicket
from rest_framework import serializers
    
class SessionTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionTicket
        fields = '__all__'