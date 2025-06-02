from .models import Session
from rest_framework import viewsets
from .serializer import  SessionSerializer
    
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer  
