from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'order'

router = routers.DefaultRouter()
router.register('', views.OrderViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls) )
]