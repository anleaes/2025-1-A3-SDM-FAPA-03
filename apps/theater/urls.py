from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'theater'

router = routers.DefaultRouter()
router.register('', views.TheaterViewSet, basename='cinemas')

urlpatterns = [
    path('', include(router.urls) )
]