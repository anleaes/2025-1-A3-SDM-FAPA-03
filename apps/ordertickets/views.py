from .models import OrderTicket
from rest_framework import viewsets
from .serializer import  OrderTicketSerializer
    
class OrderTicketViewSet(viewsets.ModelViewSet):
    queryset = OrderTicket.objects.all()
    serializer_class = OrderTicketSerializer