from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'address'

router = routers.DefaultRouter()
router.register('', views.AddressViewSet, basename='enderecos')

urlpatterns = [
    path('', include(router.urls) )
]
