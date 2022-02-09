from tkinter.tix import Select

from django.forms import *
from aplicacion.app_paciente.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'cedula': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese una cedula'
                }
            ),
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un nombre'
                }
            ),
            'apellido': DateInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un apellido'
                }
            ),
            'direccion': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese una dirección'
                }
            ),
            'ocupacion': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese una ocupacion'
                }
            ),
            'sexo': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese el sexo'
                }
            ),
            'telefono': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un telefono'
                }
            ),
            'fechaNacimiento': DateInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese una fecha de Nacimiento'
                }
            )

        }

        exclude = ['id']