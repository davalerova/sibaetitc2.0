from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Tipo_afiliacion)
class Tipo_afiliacionAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','valor_porcentaje_descuento', 'estado','fc','uc','fm','um',)

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id','beneficiario','servicio','tipo_afiliacion','inasistensias_acumuladas',
                    'inasistensias_acumuladas_justificadas','inasistensias_ultimo_mes',
                    'inasistensias_justificadas_ultimo_mes','lunes','martes','miercoles','jueves','viernes','sabado',
                    'estado','fc','uc','fm','um',)

