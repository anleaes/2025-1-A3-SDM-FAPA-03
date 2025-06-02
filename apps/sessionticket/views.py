from .models import SessionTicket
from rest_framework import viewsets
from .serializer import  SessionTicketSerializer

# Após o comentario "# Create your views here." e crie as views "Orderitem".
    
class SessionTicketViewSet(viewsets.ModelViewSet):
    queryset = SessionTicket.objects.all()
    serializer_class = SessionTicketSerializer