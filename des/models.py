from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum

import os
# Create your models here.
from bases.models import ClaseModelo
from ins.models import Inscripcion
from ben.models import Beneficiario



class Consumo( ClaseModelo ):

    inscripcion = models.ForeignKey(
        Inscripcion,
        help_text='Inscripción',
        verbose_name='Inscrición',
        on_delete=False
    )

    valor = models.PositiveIntegerField(
        help_text='Valor cancelado',
        verbose_name='Valor cancelado',
        default=0
    )

    fecha = models.DateField(
        auto_now_add=True,
        editable=False,
    )

    observacion = models.CharField(
        default='OK',
        max_length=255
    )

    def __str__(self):
        return '{} {}'.format( self.inscripcion, self.fecha)

    def save(self):
        super( Consumo, self ).save()


    class Meta:
        verbose_name = 'Consumo'
        verbose_name_plural = 'Consumos'
        unique_together = ('inscripcion', 'fecha')

@receiver(pre_save, sender=Consumo)
def descontar_saldo(sender, instance, **kwargs):
    beneficiario_id = instance.inscripcion.beneficiario.id
    valor_a_descontar = instance.inscripcion.servicio.valor - \
                      (instance.inscripcion.servicio.valor *
                       instance.inscripcion.tipo_afiliacion.valor_porcentaje_descuento / 100)
    estado = instance.estado


    ben = Beneficiario.objects.get(pk=beneficiario_id)
    if ben.saldo>=valor_a_descontar:
        if estado:
            ben.saldo-=valor_a_descontar
            ben.save()
            instance.valor = valor_a_descontar
        else:
            ben.saldo += valor_a_descontar
            ben.save()
    else:
        print('Saldo insuficiente')
        instance.valor=0
        instance.observacion='Saldo insuficiente'