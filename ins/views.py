from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import *
from .forms import *


########################################################################################################################

class Tipo_afiliacionView(LoginRequiredMixin, generic.ListView):
    model = Tipo_afiliacion
    template_name = 'ins/tipo_afiliacion_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class Tipo_afiliacionNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_afiliacion
    template_name = 'ins/tipo_afiliacion_form.html'
    context_object_name = 'obj'
    form_class = Tipo_afiliacionForm
    success_url = reverse_lazy('ins:tipo_afiliacion_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class Tipo_afiliacionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_afiliacion
    template_name = 'ins/tipo_afiliacion_form.html'
    context_object_name = 'obj'
    form_class = Tipo_afiliacionForm
    success_url = reverse_lazy('ins:tipo_afiliacion_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class Tipo_afiliacionDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_afiliacion
    template_name = 'ins/tipo_afiliacion_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ins:tipo_afiliacion_list')

########################################################################################################################

class InscripcionView(LoginRequiredMixin, generic.ListView):
    model = Inscripcion
    template_name = 'ins/inscripcion_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class InscripcionNew(LoginRequiredMixin, generic.CreateView):
    model = Inscripcion
    template_name = 'ins/inscripcion_form.html'
    context_object_name = 'obj'
    form_class = InscripcionForm
    success_url = reverse_lazy('ins:inscripcion_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class InscripcionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Inscripcion
    template_name = 'ins/inscripcion_form.html'
    context_object_name = 'obj'
    form_class = InscripcionForm
    success_url = reverse_lazy('ins:inscripcion_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class InscripcionDel(LoginRequiredMixin, generic.DeleteView):
    model = Inscripcion
    template_name = 'ins/inscripciono_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ins:inscripcion_list')



########################################################################################################################




def tipo_afiliacion_inactivar(request, id):
    tipo_afiliacion = Tipo_afiliacion.objects.filter( pk=id ).first()
    contexto = {}
    template_name = "ins/tipo_afiliacion_del.html"

    if not tipo_afiliacion:
        return redirect( "ins:tipo_afiliacion_list" )

    if request.method == 'GET':
        contexto = {'obj': tipo_afiliacion}

    if request.method == 'POST':
        tipo_afiliacion.estado = False
        tipo_afiliacion.save()
        return redirect( "ins:tipo_afiliacion_list" )

    return render( request, template_name, contexto )
########################################################################################################################
def inscripcion_inactivar(request, id):
    inscripcion = Inscripcion.objects.filter( pk=id ).first()
    contexto = {}
    template_name = "ins/inscripcion_del.html"

    if not inscripcion:
        return redirect( "ins:inscripcion_list" )

    if request.method == 'GET':
        contexto = {'obj': inscripcion}

    if request.method == 'POST':
        inscripcion.estado = False
        inscripcion.save()
        return redirect( "ins:inscripcion_list" )

    return render( request, template_name, contexto )
