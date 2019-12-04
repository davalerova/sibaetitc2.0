from django.urls import path
from .views import *

urlpatterns = [

    path('tipos_afiliaciones/', Tipo_afiliacionView.as_view(), name='tipo_afiliacion_list'),
    path('tipos_afiliaciones/new/', Tipo_afiliacionNew.as_view(), name='tipo_afiliacion_new'),
    path('tipos_afiliaciones/edit/<int:pk>', Tipo_afiliacionEdit.as_view(), name='tipo_afiliacion_edit'),
    path('tipos_afiliaciones/inactivar/<int:id>', tipo_afiliacion_inactivar, name='tipo_afiliacion_inactivar'),

    path('inscripciones/', InscripcionView.as_view(), name='inscripcion_list'),
    path('inscripciones/new/', InscripcionNew.as_view(), name='inscripcion_new'),
    path('inscripciones/edit/<int:pk>', InscripcionEdit.as_view(), name='inscripcion_edit'),
    path('inscripciones/inactivar/<int:id>', inscripcion_inactivar, name='inscripcion_inactivar'),

]
