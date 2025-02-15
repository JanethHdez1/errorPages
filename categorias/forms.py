from .models import Categoria
from django import forms

class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = ['nombre', 'imagen']

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de la categoría'
                }
            ),
            'imagen': forms.URLInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen de la categoría'
                }
            )
        }

        labels = {
            'nombre': 'Nombre de la categoría',
            'imagen': 'URL de la imagen de la categoría',
        }

        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio',
                'unique': 'Esta categoría ya existe'
            },
            'imagen': {
                'required': 'Este campo es obligatorio',
                'invalid': 'Ingrese una URL válida'
            }
        }