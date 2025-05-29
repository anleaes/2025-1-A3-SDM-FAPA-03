from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'client'

router = routers.DefaultRouter()
router.register('', views.ClientViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls) )
]