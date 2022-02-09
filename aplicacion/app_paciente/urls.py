
from django.urls import path, include
from django.views.generic import TemplateView
from aplicacion.app_paciente.views.paciente import listarPacienteView, CrearPacienteView, EditarPacienteView

app_name = 'app_paciente'

urlpatterns = [

    #path('inicio_paciente/', TemplateView.as_view(template_name = 'app_paciente/listar_paciente.html'), name='inicio_paciente'),
    path('listar/', listarPacienteView.as_view(), name='listar_paciente'),
    path('crear/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar/<int:pk>/', EditarPacienteView.as_view(), name='editar_paciente'),

]