from django.urls import path
from .views import *

urlpatterns = [

    path('consumos/', ConsumoView.as_view(), name='consumo_list'),
    path('consumos/new/', ConsumoNew.as_view(), name='consumo_new'),
    path('consumos/edit/<int:pk>', ConsumoEdit.as_view(), name='consumo_edit'),
    path('consumos/inactivar/<int:id>', consumo_inactivar, name='consumo_inactivar'),


]
