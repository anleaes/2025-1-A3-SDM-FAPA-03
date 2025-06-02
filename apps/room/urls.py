from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'room'

router = routers.DefaultRouter()
router.register('', views.RoomViewSet, basename='salas')

urlpatterns = [
    path('', include(router.urls) )
]