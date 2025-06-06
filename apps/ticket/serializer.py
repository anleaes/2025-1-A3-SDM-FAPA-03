from client.models import Client
from client.serializer import ClientSerializer
from .models import Ticket
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    clientDetail = ClientSerializer(source='client', read_only=True)
    class Meta:
        model = Ticket
        fields = ['id', 'totalPrice', 'paymentMethod', 'status', 'rating', 'client', 'clientDetail']