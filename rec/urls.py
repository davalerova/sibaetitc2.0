from django.urls import path
from .views import *

urlpatterns = [

    path('recargas/', RecargaView.as_view(), name='recarga_list'),
    path('recargas/new/', RecargaNew.as_view(), name='recarga_new'),
    path('recargas/edit/<int:pk>', RecargaEdit.as_view(), name='recarga_edit'),
    path('recargas/inactivar/<int:id>', recarga_inactivar, name='recarga_inactivar'),


]
