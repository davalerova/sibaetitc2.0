from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import *
from .forms import *


########################################################################################################################

class ServicioView(LoginRequiredMixin, generic.ListView):
    model = Servicio
    template_name = 'ser/servicio_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ServicioNew(LoginRequiredMixin, generic.CreateView):
    model = Servicio
    template_name = 'ser/servicio_form.html'
    context_object_name = 'obj'
    form_class = ServicioForm
    success_url = reverse_lazy('ser:servicio_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class ServicioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Servicio
    template_name = 'ser/servicio_form.html'
    context_object_name = 'obj'
    form_class = ServicioForm
    success_url = reverse_lazy('ser:servicio_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ServicioDel(LoginRequiredMixin, generic.DeleteView):
    model = Servicio
    template_name = 'ser/servicio_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ser:servicio_list')

########################################################################################################################

class Programacion_servicioView(LoginRequiredMixin, generic.ListView):
    model = Programacion_servicio
    template_name = 'ser/programacion_servicio_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class Programacion_servicioNew(LoginRequiredMixin, generic.CreateView):
    model = Programacion_servicio
    template_name = 'ser/programacion_servicio_form.html'
    context_object_name = 'obj'
    form_class = Programacion_servicioForm
    success_url = reverse_lazy('ser:programacion_servicio_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class Programacion_servicioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Programacion_servicio
    template_name = 'ser/programacion_servicio_form.html'
    context_object_name = 'obj'
    form_class = Programacion_servicioForm
    success_url = reverse_lazy('ser:programacion_servicio_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class Programacion_servicioDel(LoginRequiredMixin, generic.DeleteView):
    model = Programacion_servicio
    template_name = 'ser/programacion_servicio_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ser:programacion_servicio_list')



########################################################################################################################




def servicio_inactivar(request, id):
    servicio = Servicio.objects.filter( pk=id ).first()
    contexto = {}
    template_name = "ser/servicio_del.html"

    if not servicio:
        return redirect( "ser:servicio_list" )

    if request.method == 'GET':
        contexto = {'obj': servicio}

    if request.method == 'POST':
        servicio.estado = False
        servicio.save()
        return redirect( "ser:servicio_list" )

    return render( request, template_name, contexto )
########################################################################################################################
def programacion_servicio_inactivar(request, id):
    programacion_servicio = Programacion_servicio.objects.filter( pk=id ).first()
    contexto = {}
    template_name = "ser/programacion_servicio_del.html"

    if not programacion_servicio:
        return redirect( "ser:programacion_servicio_list" )

    if request.method == 'GET':
        contexto = {'obj': programacion_servicio}

    if request.method == 'POST':
        programacion_servicio.estado = False
        programacion_servicio.save()
        return redirect( "ser:programacion_servicio_list" )

    return render( request, template_name, contexto )
