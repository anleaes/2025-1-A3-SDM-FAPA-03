from django.db import models

class Address(models.Model):
    street = models.CharField('Rua', max_length=100)
    number = models.IntegerField('Número')
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=2)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.street}, {self.number} - {self.city}/{self.state}'