from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ordertickets'

router = routers.DefaultRouter()
router.register('', views.OrderTicketViewSet, basename='ingressos_pedido')

urlpatterns = [
    path('', include(router.urls) )
]