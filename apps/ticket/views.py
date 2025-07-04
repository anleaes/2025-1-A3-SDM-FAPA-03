from .models import Ticket
from rest_framework import viewsets
from .serializer import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer  