from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum

import os
# Create your models here.
from bases.models import ClaseModelo
from ben.models import Beneficiario


class Recarga( ClaseModelo ):

    beneficiario = models.ForeignKey(
        Beneficiario,
        help_text='Nombre del beneficiario',
        verbose_name='Nombre beneficiario',
        on_delete=False
    )

    valor = models.PositiveIntegerField(
        help_text='Valor recarga',
        verbose_name='Valor recarga'
    )

    def __str__(self):
        return '{} {}'.format( self.beneficiario, self.valor)

    def save(self):
        super( Recarga, self ).save()


    class Meta:
        verbose_name = 'Recarga'
        verbose_name_plural = 'Recargas'

@receiver(pre_save, sender=Recarga)
def recargar_saldo(sender, instance, **kwargs):
    id = instance.beneficiario.id
    valor = instance.valor
    estado = instance.estado

    ben = Beneficiario.objects.get(pk=id)
    if ben.estado:
        if estado:
            ben.saldo+=valor
            ben.save()
        else:
            ben.saldo -= valor
            ben.save()
    else:
        print('El beneficiario {} no se encuentra activo'.format(ben))
        instance.valor=0