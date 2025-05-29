from django.db import models
from ticket.models import Ticket
from order.models import Order


class OrderTicket(models.Model):
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Ingresso')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Pedido')
    
    class Meta:
        unique_together = ('ticket', 'order')
        verbose_name = 'Ingresso do Pedido'
        verbose_name_plural = 'Ingressos do Pedido'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"


