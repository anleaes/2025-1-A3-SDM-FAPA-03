from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'sessionticket'

router = routers.DefaultRouter()
router.register('', views.SessionTicketViewSet, basename='ingressos-da-sessao')

urlpatterns = [
    path('', include(router.urls) )
]