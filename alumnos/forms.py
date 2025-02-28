from .models import Alumno
from django import forms

#Crear una clase por cada formulario que necesitemos
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del Alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido del Alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la edad del Alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la matrícula del Alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo del Alumno'
                }
            )
        }

        labels = {
            'nombre': 'Nombre del Alumno',
            'apellido': 'Apellido del Alumno',
            'edad': 'Edad del Alumno',
            'matricula': 'Matrícula del Alumno',
            'correo': 'Correo del Alumno'
        }

        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio',
                'unique': 'Este Alumno ya existe'
            },
            'apellido': {
                'required': 'Este campo es obligatorio'
            },
            'edad': {
                'required': 'Este campo es obligatorio'
            },
            'matricula': {
                'required': 'Este campo es obligatorio',
                'unique': 'Esta matrícula ya existe'
            },
            'correo': {
                'required': 'Este campo es obligatorio',
                'unique': 'Este correo ya existe'
            }
        }