from django.db import models

from django.db import models

class SessionTicket(models.Model):
    session = models.ForeignKey('Session', on_delete=models.CASCADE, verbose_name='Sessão')
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, verbose_name='Ingresso')
    quantity = models.PositiveIntegerField('Quantidade')
    unitary_price = models.DecimalField('Preço Unitário', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Ingresso da Sessão'
        verbose_name_plural = 'Ingressos da Sessão'
        ordering = ['id']

    def __str__(self):
        return f'{self.quantity}x {self.ticket.movie.title} - Sessão {self.session.id}'

