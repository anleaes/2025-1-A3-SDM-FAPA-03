from django.db import models

class Gender(models.Model):
    POPULARITY_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )

    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=200)
    isActive = models.BooleanField('Ativo', default=True)
    popularity = models.CharField('Popularidade', max_length=1, choices=POPULARITY_CHOICES)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['id']

    def __str__(self):
        return self.name

