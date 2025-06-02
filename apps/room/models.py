from django.db import models

class Room(models.Model):
    ROOM_TYPE_CHOICES = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
        ('VIP', 'VIP'),
    )

    number = models.IntegerField('Número da Sala')
    type = models.CharField('Tipo', max_length=10, choices=ROOM_TYPE_CHOICES)
    accessibility = models.BooleanField('Acessibilidade', default=False)
    capacity = models.PositiveIntegerField('Capacidade')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['number']

    def __str__(self):
        return f'Sala {self.number} ({self.type})'

