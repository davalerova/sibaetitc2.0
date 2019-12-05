from django import forms
from django.db import *

from .models import *
from ben.models import Beneficiario
from ser.models import Servicio
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
    beneficiario = forms.ModelChoiceField(
        queryset=Beneficiario.objects.filter( estado=True )
            .order_by( 'rfid' )
    )

    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter( estado=True )
            .order_by( 'descripcion' )
    )

    tipo_afiliacion = forms.ModelChoiceField(
        queryset=Tipo_afiliacion.objects.filter( estado=True )
            .order_by( 'descripcion' )
    )
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

