from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum

import os
# Create your models here.
from bases.models import ClaseModelo
from ins.models import Inscripcion


class Motivo_suspension( ClaseModelo ):

    descripcion = models.CharField(max_length=50,
        help_text='Descripción motivo suspensión',
        verbose_name='Descripción'
    )

    duracion = models.PositiveIntegerField(
        help_text='Duración de la suspensión en días',
        verbose_name='Duración suspensión'
    )

    def __str__(self):
        return '{} {}'.format( self.inscripcion, self.motivo)

    def save(self):
        super( Suspension, self ).save()


    class Meta:
        verbose_name = 'Motivo suspensión'
        verbose_name_plural = 'Motivo suspensiones'

########################################################################################################################
class Suspension( ClaseModelo ):

    inscripcion = models.ForeignKey(
        Inscripcion,
        help_text='Inscripción',
        verbose_name='Inscripción',
        on_delete=False
    )

    motivo = models.ForeignKey(
        Motivo_suspension, on_delete=False
    )

    descripcion = models.TextField(
        help_text='Descripción del motivo de la suspensión'
    )

    def __str__(self):
        return '{} {}'.format( self.inscripcion, self.motivo)

    def save(self):
        super( Suspension, self ).save()


    class Meta:
        verbose_name = 'Suspension'
        verbose_name_plural = 'Suspensiones'
