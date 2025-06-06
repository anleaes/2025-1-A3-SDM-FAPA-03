from session.serializer import SessionSerializer
from ticket.serializer import TicketSerializer
from session.models import Session
from ticket.models import Ticket
from .models import SessionTicket
from rest_framework import serializers
    
class SessionTicketSerializer(serializers.ModelSerializer):
    session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())
    sessionDetail = SessionSerializer(source='session', read_only=True)
    ticketDetail = TicketSerializer(source='ticket', read_only=True)

    class Meta:
        model = SessionTicket
        fields = ['id', 'session', 'ticket', 'quantity', 'unitaryPrice', 'sessionDetail', 'ticketDetail']