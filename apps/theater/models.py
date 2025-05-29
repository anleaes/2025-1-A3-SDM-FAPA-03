from django.db import models
from address.models import Address
from movie.models import Movie

class Theater(models.Model):
    name = models.CharField('Nome', max_length=100)
    openingHours = models.CharField('Horário de Abertura', max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Endereço')
    contact_number = models.CharField('Telefone de Contato', max_length=20)
    movies = models.ManyToManyField(Movie, verbose_name='Filmes em Cartaz')

    class Meta:
        verbose_name = 'Cinema'
        verbose_name_plural = 'Cinemas'
        ordering = ['id']

    def __str__(self):
        return f'Cinema - {self.address}'
