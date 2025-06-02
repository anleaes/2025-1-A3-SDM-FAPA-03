from django.db import models
from theater.models import Theater
from movie.models import Movie
from room.models import Room


class Session(models.Model):
    LANGUAGE_CHOICES = (
        ('DUB', 'Dublado'),
        ('LEG', 'Legendado'),
        ('ORI', 'Original'),
    )

    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, verbose_name='Cinema')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Filme')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Sala')
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)
    language = models.CharField('Idioma', max_length=3, choices=LANGUAGE_CHOICES)

    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'
        ordering = ['id']

    def __str__(self):
        return f'{self.movie.title} - Sala {self.room.number} ({self.language})'

