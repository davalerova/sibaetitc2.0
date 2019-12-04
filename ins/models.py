import os
# Create your models here.
from django.db import models
from bases.models import ClaseModelo
from datetime import datetime
from ben.models import Beneficiario
from ser.models import Servicio

class Tipo_afiliacion( ClaseModelo ):

    descripcion = models.CharField(
        help_text='Descripción del tipo de afiliación',
        verbose_name='Descripción del tipo de afiliación',
        max_length=45,
        unique=True
    )

    valor_porcentaje_descuento = models.IntegerField(
        help_text='Valor del porcentaje de descuento del tipo de afiliación',
        verbose_name='Porcentaje descuento'
    )

    def __str__(self):
        return '{} {}'.format(self.descripcion, self.valor_porcentaje_descuento)
    class Meta:
        verbose_name = 'Tipo de afiliación'
        verbose_name_plural = 'Tipos de afiliación'
        unique_together = ('descripcion', 'valor_porcentaje_descuento',)

########################################################################################################################

class Inscripcion( ClaseModelo ):

    beneficiario = models.ForeignKey(
        Beneficiario,
        help_text='Beneficiario inscripción',
        verbose_name='Beneficiario inscripción',
        on_delete=False
    )
    servicio = models.ForeignKey(
        Servicio,
        help_text='Servicio inscripción',
        verbose_name='Servicio inscripción',
        on_delete=False
    )
    tipo_afiliacion = models.ForeignKey(
        Tipo_afiliacion,
        help_text='Tipo de afiliación',
        verbose_name='Tipo de afiliación',
        on_delete=False
    )

    inasistensias_acumuladas = models.PositiveIntegerField(
        help_text='Fallas acumuladas por cada servicio',
        verbose_name='Fallas acumuladas',
        editable=False,
        default=0
    )

    inasistensias_acumuladas_justificadas = models.PositiveIntegerField(
        help_text='Fallas acumuladas con justificación por cada servicio',
        verbose_name='Fallas acumuladas justificadas',
        editable=False,
        default=0
    )

    inasistensias_ultimo_mes = models.PositiveIntegerField(
        help_text='Fallas por cada servicio durante el último mes',
        verbose_name='Fallas mes',
        editable=False,
        default=0
    )

    inasistensias_justificadas_ultimo_mes = models.PositiveIntegerField(
        help_text='Fallas acumuladas con justificación por cada servicio en el último mes',
        verbose_name='Fallas acumuladas justificadas mes',
        editable=False,
        default=0
    )


    lunes = models.BooleanField(
        help_text='El servicio se toma el lunes',
        verbose_name='Lunes',
        default=True
    )

    martes = models.BooleanField(
        help_text='El servicio se toma el martes',
        verbose_name='martes',
        default=True
    )

    miercoles = models.BooleanField(
        help_text='El servicio se toma el miércoles',
        verbose_name='Miercoles',
        default=True
    )

    jueves = models.BooleanField(
        help_text='El servicio se toma el jueves',
        verbose_name='Jueves',
        default=True
    )

    viernes = models.BooleanField(
        help_text='El servicio se toma el viernes',
        verbose_name='Viernes',
        default=True
    )

    sabado = models.BooleanField(
        help_text='El servicio se toma el sábado',
        verbose_name='Sábado',
        default=False
    )




    def __str__(self):
        return '{} {} {}'.format( self.beneficiario, self.servicio, self.tipo_afiliacion )


    class Meta:
        verbose_name = 'Inscripción servicio'
        verbose_name_plural = 'Inscripciones Servicios'
        unique_together = ('beneficiario', 'servicio', 'tipo_afiliacion',)
########################################################################################################################
