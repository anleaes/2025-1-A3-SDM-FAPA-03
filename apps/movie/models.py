from django.db import models

class Movie(models.Model):
    title = models.CharField('Título', max_length=100)
    duration = models.IntegerField('Duração (minutos)')
    description = models.TextField('Descrição', max_length=500)
    poster = models.ImageField('Pôster', upload_to='posters/')

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['id']

    def __str__(self):
        return self.title