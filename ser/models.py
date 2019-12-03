import os
# Create your models here.
from django.db import models
from bases.models import ClaseModelo
from datetime import datetime


class Servicio( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Nombre del servicio',
        unique=True,
        verbose_name='Nombre servicio'
    )

    hora_inicio = models.TimeField(
        help_text='Hora de inicio',
        verbose_name='Hora inicio'
    )

    hora_fin = models.TimeField(
        help_text='Hora de fin',
        verbose_name='Hora fin'
    )

    valor = models.PositiveIntegerField(
        help_text='Valor del servicio',
        verbose_name='Valor servicio'
    )

    lunes = models.BooleanField(
        help_text='El servicio se presta el lunes',
        verbose_name='Lunes',
        default=True
    )

    martes = models.BooleanField(
        help_text='El servicio se presta el martes',
        verbose_name='martes',
        default=True
    )

    miercoles = models.BooleanField(
        help_text='El servicio se presta el miércoles',
        verbose_name='Miercoles',
        default=True
    )

    jueves = models.BooleanField(
        help_text='El servicio se presta el jueves',
        verbose_name='Jueves',
        default=True
    )

    viernes = models.BooleanField(
        help_text='El servicio se presta el viernes',
        verbose_name='Viernes',
        default=True
    )

    sabado = models.BooleanField(
        help_text='El servicio se presta el sábado',
        verbose_name='Sábado',
        default=True
    )




    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Servicio, self ).save()

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
########################################################################################################################

class Programacion_servicio( ClaseModelo ):

    servicio = models.ForeignKey(
        Servicio,
        help_text='Servicio a programar',
        verbose_name='Servicio a programar',
        on_delete=False
    )

    fecha = models.DateField(
        help_text='Fecha en que se programa prestar un servicio',
        verbose_name='Fecha programacion servicio',
        default=datetime.now()

    )


    def __str__(self):
        return '{} {}'.format( self.servicio,self.fecha)


    class Meta:
        verbose_name = 'Programación Servicio'
        verbose_name_plural = 'Programación Servicios'