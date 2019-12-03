from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado','fc','uc','fm','um',)

@admin.register(Documento)
class Documento_identidadAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado','fc','uc','fm','um',)

@admin.register(Tipo_beneficiario)
class Tipo_beneficiarioAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado','fc','uc','fm','um',)

@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado','fc','uc','fm','um',)

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'rfid', 'documento', 'numero_documento', 'genero',
                    'dependencia', 'tipo_beneficiario', 'nombres', 'apellidos','email', 'fecha_nacimiento',
                    'saldo', 'foto', 'estado','fc','uc','fm','um',)