from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','hora_inicio','hora_fin','valor','lunes','martes','miercoles','jueves',
                    'viernes','sabado','estado','fc','uc','fm','um',)

@admin.register(Programacion_servicio)
class Programacion_servicioAdmin(admin.ModelAdmin):
    list_display = ('id','servicio','fecha','estado','fc','uc','fm','um',)

