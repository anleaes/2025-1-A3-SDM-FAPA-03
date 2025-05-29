from django.db import models
from client.models import Client

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    status = models.BooleanField('Status', default=False)
    total_price = models.DecimalField('Preço Total', max_digits=8, decimal_places=2)
    date = models.DateField('Data do Pedido', auto_now_add=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def __str__(self):
        return f'Pedido #{self.id} - {self.client.name}'
