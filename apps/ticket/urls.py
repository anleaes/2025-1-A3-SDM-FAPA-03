from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ticket'

router = routers.DefaultRouter()
router.register('', views.TicketViewSet, basename='ingressos')

urlpatterns = [
    path('', include(router.urls) )
]