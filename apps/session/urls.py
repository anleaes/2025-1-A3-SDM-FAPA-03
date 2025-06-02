from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'session'

router = routers.DefaultRouter()
router.register('', views.SessionViewSet, basename='sessoes')

urlpatterns = [
    path('', include(router.urls) )
]