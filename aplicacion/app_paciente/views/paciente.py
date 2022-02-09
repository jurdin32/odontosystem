
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from aplicacion.app_paciente.forms import PacienteForm
from aplicacion.app_paciente.models import Paciente
# Create your views here.


class listarPacienteView(ListView):
    model = Paciente
    template_name = 'app_paciente/listar_paciente.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pacientes'
        return context


class CrearPacienteView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'app_paciente/crear_paciente.html'
    success_url = reverse_lazy('app_paciente:listar_paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Datos del Paciente'
        return context


class EditarPacienteView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'app_paciente/editar_paciente.html'
    success_url = reverse_lazy('app_paciente:listar_paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Datos del Paciente'
        return context