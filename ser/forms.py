from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class ServicioForm( forms.ModelForm ):
    class Meta:
        model = Servicio
        fields = ['descripcion','hora_inicio','hora_fin','valor','lunes','martes','miercoles', 'jueves', 'viernes', 'sabado', 'estado']
        labels = {'descripcion': "Descripción del servicio", "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class Programacion_servicioForm( forms.ModelForm ):
    class Meta:
        model = Programacion_servicio
        fields = ['servicio', 'fecha' ,'estado']
        labels = {'servicio': "Servicio", "estado": "Estado"}
        widget = {'fecha': forms.DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )

