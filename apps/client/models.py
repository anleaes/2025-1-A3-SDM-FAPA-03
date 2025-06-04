from django.db import models

class Client(models.Model):
    email = models.EmailField('E-mail', null=False, blank=False)
    name = models.CharField('Nome', max_length=100)
    isActive = models.BooleanField('Ativo', default=True)

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Gênero', max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.name
