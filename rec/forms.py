from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class RecargaForm( forms.ModelForm ):
    class Meta:
        model = Recarga
        fields = ['beneficiario','valor','estado']
        labels = {'beneficiario': "Beneficiario", "estado": "Estado"}
        widget = {'valor': forms.IntegerField}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )
