from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class ConsumoForm( forms.ModelForm ):
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
