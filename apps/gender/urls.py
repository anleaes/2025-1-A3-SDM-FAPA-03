from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'gender'

router = routers.DefaultRouter()
router.register('', views.GenderViewSet, basename='generos')

urlpatterns = [
    path('', include(router.urls) )
]
