from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class Tipo_afiliacionForm( forms.ModelForm ):
    class Meta:
        model = Tipo_afiliacion
        fields = ['descripcion','valor_porcentaje_descuento','estado']
        labels = {'descripcion': "Descripción del servicio", "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class InscripcionForm( forms.ModelForm ):
    class Meta:
        model = Inscripcion
        fields = ['beneficiario', 'servicio' ,'tipo_afiliacion'  ,'lunes' ,'martes' , 'miercoles','jueves','viernes','sabado','estado',]
        labels = {'servicio': "Servicio", "estado": "Estado"}
        widget = {'lunes':forms.BooleanField}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )

