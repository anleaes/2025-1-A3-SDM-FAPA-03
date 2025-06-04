from django.db import models
from session.models import Session
from ticket.models import Ticket

class SessionTicket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='Sessão')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Ingresso')
    quantity = models.PositiveIntegerField('Quantidade')
    unitaryPrice = models.DecimalField('Preço Unitário', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Ingresso da Sessão'
        verbose_name_plural = 'Ingressos da Sessão'
        ordering = ['id']

    def __str__(self):
        return f'{self.ticket.client.name} - Sessão {self.session.movie.title}'

