from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import *
from .forms import *


########################################################################################################################

class RecargaView(LoginRequiredMixin, generic.ListView):
    model = Recarga
    template_name = 'rec/recarga_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class RecargaNew(LoginRequiredMixin, generic.CreateView):
    model = Recarga
    template_name = 'rec/recarga_form.html'
    context_object_name = 'obj'
    form_class = RecargaForm
    success_url = reverse_lazy('rec:recarga_new')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class RecargaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Recarga
    template_name = 'rec/recarga_form.html'
    context_object_name = 'obj'
    form_class = RecargaForm
    success_url = reverse_lazy('rec:recarga_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class RecargaDel(LoginRequiredMixin, generic.DeleteView):
    model = Recarga
    template_name = 'rec/recarga_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('rec:recarga_list')

########################################################################################################################


def recarga_inactivar(request, id):
    recarga = Recarga.objects.filter( pk=id ).first()
    contexto = {}
    template_name = "rec/recarga_del.html"

    if not recarga:
        return redirect( "rec:recarga_list" )

    if request.method == 'GET':
        contexto = {'obj': recarga}

    if request.method == 'POST':
        recarga.estado = False
        recarga.save()
        return redirect( "rec:recarga_list" )

    return render( request, template_name, contexto )
