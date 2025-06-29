from django.shortcuts import render

from .models import Gender
from rest_framework import viewsets
from .serializer import GenderSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer 
