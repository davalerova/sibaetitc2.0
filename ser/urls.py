from django.urls import path
from .views import *

urlpatterns = [

    path('servicios/', ServicioView.as_view(), name='servicio_list'),
    path('servicios/new/', ServicioNew.as_view(), name='servicio_new'),
    path('servicios/edit/<int:pk>', ServicioEdit.as_view(), name='servicio_edit'),
    path('servicios/inactivar/<int:id>', servicio_inactivar, name='servicio_inactivar'),

    path('programacion_servicios/', Programacion_servicioView.as_view(), name='programacion_servicio_list'),
    path('programacion_servicios/new/', Programacion_servicioNew.as_view(), name='programacion_servicio_new'),
    path('programacion_servicios/edit/<int:pk>', Programacion_servicioEdit.as_view(), name='programacion_servicio_edit'),
    path('programacion_servicios/inactivar/<int:id>', programacion_servicio_inactivar, name='programacion_servicio_inactivar'),

]
