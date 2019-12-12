from django import forms
from django.db import *
from ins.models import Inscripcion

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class ConsumoForm( forms.ModelForm ):
    inscripcion = forms.ModelChoiceField(
        queryset=Inscripcion.objects.filter( estado=True )
            .order_by( 'beneficiario' )
    )
    class Meta:
        model = Consumo
        fields = ['inscripcion','estado']
        labels = {'inscripcion': "Inscripcion", "estado": "Estado"}
        widget = {'estado': forms.BooleanField}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )
