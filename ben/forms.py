from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class GeneroForm( forms.ModelForm ):
    class Meta:
        model = Genero
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción del género", "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class DocumentoForm( forms.ModelForm ):
    class Meta:
        model = Documento
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripcion del documento de identidad", "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class Tipo_beneficiarioForm( forms.ModelForm ):
    class Meta:
        model = Tipo_beneficiario
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripcion del tipo de beneficiario", "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class DependenciaForm( forms.ModelForm ):
    class Meta:
        model = Dependencia
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripcion de la dependencia", "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )

########################################################################################################################

class BeneficiarioForm( forms.ModelForm ):
    documento = forms.ModelChoiceField(
        queryset=Documento.objects.filter( estado=True )
            .order_by( 'descripcion' )
    )
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.filter( estado=True )
            .order_by( 'descripcion' )
    )
    dependencia = forms.ModelChoiceField(
        queryset=Dependencia.objects.filter( estado=True )
            .order_by( 'descripcion' )
    )
    tipo_beneficiario = forms.ModelChoiceField(
        queryset=Tipo_beneficiario.objects.filter( estado=True )
            .order_by( 'descripcion' )
    )

    class Meta:
        model = Beneficiario
        fields = ['rfid', 'documento', 'numero_documento',
                  'genero', 'dependencia', 'tipo_beneficiario', 'nombres',
                  'apellidos', 'email', 'fecha_nacimiento', 'foto',
                  'estado']
        labels = {'estado': 'Estado'}
        widget = {'rfid': forms.TextInput,
                  'foto': forms.ImageField,
                  }

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )
