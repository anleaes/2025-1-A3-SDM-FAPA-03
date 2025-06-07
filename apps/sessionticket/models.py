from datetime import date
from django.db import models
from session.models import Session
from ticket.models import Ticket

class SessionTicket(models.Model):
    TICKET_TYPE_CHOICES = (
        ('inteira', 'Inteira'),
        ('meia', 'meia'),
        ('cortesia', 'Cortesia'),
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='Sessão')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Ingresso')
    type = models.CharField('Tipo', max_length=10, choices=TICKET_TYPE_CHOICES, default='inteira')
    dateOfPurchase = models.DateField('Data de Compra', default=date.today)

    class Meta:
        verbose_name = 'Ingresso da Sessão'
        verbose_name_plural = 'Ingressos da Sessão'
        ordering = ['id']

    def __str__(self):
        return f'{self.ticket.client.name} - Sessão {self.session.movie.title}'

