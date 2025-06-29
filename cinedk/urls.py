"""
URL configuration for cinedk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmes/', include('movie.urls', namespace='filmes')),
    path('clientes/', include('client.urls', namespace='clientes')),
    path('ingressos/', include('ticket.urls', namespace='ingressos')),
    path('cinemas/', include('theater.urls', namespace='cinemas')),
    path('gêneros/', include('gender.urls', namespace='gêneros')),
    path('salas/', include('room.urls', namespace='salas')),
    path('sessões/', include('session.urls', namespace='sessões')),
    path('ingressos-da-sessão/', include('sessionticket.urls', namespace='ingressos-da-sessão')),
]

#declararando a pasta caminho e raiz para arquivos que sera enviados 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)