from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Recarga)
class RecargaAdmin(admin.ModelAdmin):
    list_display = ('id','beneficiario','valor','estado','fc','uc','fm','um',)

