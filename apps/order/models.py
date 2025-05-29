from django.db import models
from client.models import Client

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    total_price = models.DecimalField('Preço Total', max_digits=8, decimal_places=2)
    payment_method = models.CharField('Forma de Pagamento', max_length=30, default='pix', choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),
    ])
    status = models.CharField('Status', max_length=20, default='andamento', choices=[
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def __str__(self):
        return f'Pedido #{self.id} - {self.client.name}'
