from django.db import models
from client.models import Client

class Ticket(models.Model):
    totalPrice = models.DecimalField(
        'Preço Total', max_digits=6, decimal_places=2)

    paymentMethod = models.CharField('Forma de Pagamento', max_length=30, default='pix', choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),
    ])
    status = models.CharField('Status', max_length=20, default='pendente', choices=[
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ])

    rating = models.CharField('Classificação', max_length=2, default='L', choices=[
        ('L', 'Livre (todas as idades)'),
        ('10', '10 anos'),
        ('12', '12 anos'),
        ('14', '14 anos'),
        ('16', '16 anos'),
        ('18', '18 anos'),
    ])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')

    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['id']

    def __str__(self):
        return f'Cod. {self.id} - Pagamento {self.status}'
