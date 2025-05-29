from django.db import models
from movie.models import Movie

class Ticket(models.Model):
    unitary_price = models.DecimalField('Preço Unitário', max_digits=6, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Filme')
    room = models.IntegerField('Sala')

    RATING_CHOICES = (
        ('L', 'Livre (todas as idades)'),
        ('10', '10 anos'),
        ('12', '12 anos'),
        ('14', '14 anos'),
        ('16', '16 anos'),
        ('18', '18 anos'),
    )
    rating = models.CharField('Classificação', max_length=2, choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['id']

    def __str__(self):
        return f'{self.movie.title} - Sala {self.room}'
