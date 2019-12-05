from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('id','inscripcion','fecha','valor','estado','fc','uc','fm','um',)

