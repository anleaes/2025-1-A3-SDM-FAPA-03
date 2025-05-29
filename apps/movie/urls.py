from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'movie'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='filmes')

urlpatterns = [
    path('', include(router.urls) )
]