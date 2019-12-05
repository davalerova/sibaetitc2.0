from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import *
from .forms import *


########################################################################################################################

class ConsumoView(LoginRequiredMixin, generic.ListView):
    model = Consumo
    template_name = 'des/consumo_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ConsumoNew(LoginRequiredMixin, generic.CreateView):
    model = Consumo
    template_name = 'des/consumo_form.html'
    context_object_name = 'obj'
    form_class = ConsumoForm
    success_url = reverse_lazy('des:consumo_new')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class ConsumoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Consumo
    template_name = 'des/consumo_form.html'
    context_object_name = 'obj'
    form_class = ConsumoForm
    success_url = reverse_lazy('des:consumo_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ConsumoDel(LoginRequiredMixin, generic.DeleteView):
    model = Consumo
    template_name = 'des/consumo_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('des:consumo_list')

########################################################################################################################


def consumo_inactivar(request, id):
    consumo = Consumo.objects.filter( pk=id ).first()
    contexto = {}
    template_name = "des/consumo_del.html"

    if not consumo:
        return redirect( "des:consumo_list" )

    if request.method == 'GET':
        contexto = {'obj': consumo}

    if request.method == 'POST':
        consumo.estado = False
        consumo.save()
        return redirect( "des:consumo_list" )

    return render( request, template_name, contexto )
