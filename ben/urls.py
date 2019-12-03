from django.urls import path
from .views import *

urlpatterns = [
    path('generos/', GeneroView.as_view(), name='genero_list'),
    path('generos/new/', GeneroNew.as_view(), name='genero_new'),
    path('generos/edit/<int:pk>', GeneroEdit.as_view(), name='genero_edit'),
    path('generos/inactivar/<int:id_genero>', genero_inactivar, name='genero_inactivar'),

    path( 'documentos/', DocumentoView.as_view(), name='documento_list'),
    path( 'documentos/new/', DocumentoNew.as_view(), name='documento_new'),
    path( 'documentos/edit/<int:pk>', DocumentoEdit.as_view(), name='documento_edit'),
    path( 'documentos/inactivar/<int:id_documento_identidad>', documento_inactivar, name='documento_inactivar'),

    path( 'tipos_beneficiario/', Tipo_beneficiarioView.as_view(), name='tipo_beneficiario_list'),
    path( 'tipos_beneficiario/new/', Tipo_beneficiarioNew.as_view(), name='tipo_beneficiario_new'),
    path( 'tipos_beneficiario/edit/<int:pk>', Tipo_beneficiarioEdit.as_view(), name='tipo_beneficiario_edit'),
    path( 'tipos_beneficiario/delete/<int:pk>', Tipo_beneficiarioDel.as_view(), name='tipo_beneficiario_del'),

    path('dependencias/', DependenciaView.as_view(), name='dependencia_list'),
    path('dependencias/new/', DependenciaNew.as_view(), name='dependencia_new'),
    path('dependencias/edit/<int:pk>', DependenciaEdit.as_view(), name='dependencia_edit'),
    path('dependencias/inactivar/<int:id_dependencia>', dependencia_inactivar, name='dependencia_inactivar'),

    path('beneficiarios/', BeneficiarioView.as_view(), name='beneficiario_list'),
    path('beneficiarios/new/', BeneficiarioNew.as_view(), name='beneficiario_new'),
    path('beneficiarios/edit/<int:pk>', BeneficiarioEdit.as_view(), name='beneficiario_edit'),
    path('beneficiarios/delete/<int:pk>', BeneficiarioDel.as_view(), name='beneficiario_del'),
]
