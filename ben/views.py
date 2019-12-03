from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import *
from .forms import *


########################################################################################################################

class GeneroView(LoginRequiredMixin, generic.ListView):
    model = Genero
    template_name = 'ben/genero_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class GeneroNew(LoginRequiredMixin, generic.CreateView):
    model = Genero
    template_name = 'ben/genero_form.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('ben:genero_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class GeneroEdit(LoginRequiredMixin, generic.UpdateView):
    model = Genero
    template_name = 'ben/genero_form.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('ben:genero_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class GeneroDel(LoginRequiredMixin, generic.DeleteView):
    model = Genero
    template_name = 'ben/genero_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ben:genero_list')

########################################################################################################################

class DocumentoView(LoginRequiredMixin, generic.ListView):
    model = Documento
    template_name = 'ben/documento_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class DocumentoNew(LoginRequiredMixin, generic.CreateView):
    model = Documento
    template_name = 'ben/documento_form.html'
    context_object_name = 'obj'
    form_class = DocumentoForm
    success_url = reverse_lazy('ben:tipo_beneficiario_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class DocumentoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Documento
    template_name = 'ben/documento_form.html'
    context_object_name = 'obj'
    form_class = DocumentoForm
    success_url = reverse_lazy('ben:documento_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class DocumentoDel(LoginRequiredMixin, generic.DeleteView):
    model = Documento
    template_name = 'ben/documento_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ben:tipo_beneficiario_list')



########################################################################################################################

class Tipo_beneficiarioView(LoginRequiredMixin, generic.ListView):
    model = Tipo_beneficiario
    template_name = 'ben/tipo_ben_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class Tipo_beneficiarioNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_beneficiario
    template_name = 'ben/tipo_beneficiario_form.html'
    context_object_name = 'obj'
    form_class = Tipo_beneficiarioForm
    success_url = reverse_lazy('ben:tipo_beneficiario_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class Tipo_beneficiarioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_beneficiario
    template_name = 'ben/tipo_beneficiario_form.html'
    context_object_name = 'obj'
    form_class = Tipo_beneficiarioForm
    success_url = reverse_lazy('ben:tipo_beneficiario_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class Tipo_beneficiarioDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_beneficiario
    template_name = 'ben/tipo_beneficiario_form.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ben:tipo_beneficiario_list')


########################################################################################################################


class DependenciaView(LoginRequiredMixin, generic.ListView):
    model = Dependencia
    template_name = 'ben/dependencia_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class DependenciaNew(LoginRequiredMixin, generic.CreateView):
    model = Dependencia
    template_name = 'ben/dependencia_form.html'
    context_object_name = 'obj'
    form_class = DependenciaForm
    success_url = reverse_lazy('ben:dependencia_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class DependenciaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Dependencia
    template_name = 'ben/dependencia_form.html'
    context_object_name = 'obj'
    form_class = DependenciaForm
    success_url = reverse_lazy('ben:dependencia_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)






########################################################################################################################


class BeneficiarioView(LoginRequiredMixin, generic.ListView):
    model = Beneficiario
    template_name = 'ben/beneficiario_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class BeneficiarioNew(LoginRequiredMixin, generic.CreateView):
    model = Beneficiario
    template_name = 'ben/beneficiario_form.html'
    context_object_name = 'obj'
    form_class = BeneficiarioForm
    success_url = reverse_lazy('ben:beneficiario_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user.id
        return super().form_valid(form)

class BeneficiarioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Beneficiario
    template_name = 'ben/beneficiario_form.html'
    context_object_name = 'obj'
    form_class = BeneficiarioForm
    success_url = reverse_lazy('ben:beneficiario_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class BeneficiarioDel(LoginRequiredMixin, generic.DeleteView):
    model = Beneficiario
    template_name = 'ben/beneficiario_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('ben:beneficiario_list')




def dependencia_inactivar(request, id_dependencia):
    dependencia = Dependencia.objects.filter( pk=id_dependencia ).first()
    contexto = {}
    template_name = "ben/dependencia_del.html"

    if not dependencia:
        return redirect( "ben:dependencia_list" )

    if request.method == 'GET':
        contexto = {'obj': dependencia}

    if request.method == 'POST':
        dependencia.estado = False
        dependencia.save()
        return redirect( "ben:dependencia_list" )

    return render( request, template_name, contexto )
########################################################################################################################
def genero_inactivar(request, id_genero):
    genero = Genero.objects.filter( pk=id_genero ).first()
    contexto = {}
    template_name = "ben/genero_del.html"

    if not genero:
        return redirect( "ben:genero_list" )

    if request.method == 'GET':
        contexto = {'obj': genero}

    if request.method == 'POST':
        genero.estado = False
        genero.save()
        return redirect( "ben:genero_list" )

    return render( request, template_name, contexto )

########################################################################################################################
def documento_inactivar(request, id_documento_identidad):
    documento = Documento.objects.filter( pk=id_documento_identidad ).first()
    contexto = {}
    template_name = "ben/documento_del.html"

    if not documento:
        return redirect( "ben:documento_list" )

    if request.method == 'GET':
        contexto = {'obj': documento}

    if request.method == 'POST':
        documento.estado = False
        documento.save()
        return redirect( "ben:documento_list" )

    return render( request, template_name, contexto )
