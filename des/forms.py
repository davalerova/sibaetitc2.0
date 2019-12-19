from django import forms
from django.db import *
from ins.models import Inscripcion
from datetime import date

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class ConsumoForm( forms.ModelForm ):
    dia = date.weekday( date.today() )
    if dia == 0:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__lunes=True, estado=True, )
                .order_by( 'beneficiario' )
        )
    elif dia == 1:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__martes=True, estado=True )
                .order_by( 'beneficiario' )
        )
    elif dia == 2:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__miercoles=True, estado=True )
                .order_by( 'beneficiario' )
        )
    elif dia == 3:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__jueves=True, estado=True )
                .order_by( 'beneficiario' )
        )
    elif dia == 4:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__viernes=True, estado=True )
                .order_by( 'beneficiario' )
        )
    elif dia == 5:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__sabado=True, estado=True )
                .order_by( 'beneficiario' )
        )
    else:
        inscripcion = forms.ModelChoiceField(
            queryset=Inscripcion.objects.filter( servicio__domingo=True, estado=True )
                .order_by( 'beneficiario' )
        )

    class Meta:
        model = Consumo
        fields = ['inscripcion', 'estado']
        labels = {'inscripcion': "Inscripcion", "estado": "Estado"}
        widget = {'estado': forms.BooleanField}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )
