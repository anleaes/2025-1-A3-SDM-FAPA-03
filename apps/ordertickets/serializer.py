from .models import OrderTicket
from rest_framework import serializers
    
class OrderTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTicket