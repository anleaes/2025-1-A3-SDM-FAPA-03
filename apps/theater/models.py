from django.db import models

class Theater(models.Model):
    name = models.CharField('Nome', max_length=100)
    openingHours = models.CharField('Horário de Abertura', max_length=50)
    address = models.CharField('Endereço', max_length=100)
    contact_number = models.CharField('Telefone de Contato', max_length=20)

    class Meta:
        verbose_name = 'Cinema'
        verbose_name_plural = 'Cinemas'
        ordering = ['id']

    def __str__(self):
        return f'Cinema - {self.address}'
