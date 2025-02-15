#Vamos a crear formularios para cada módulo de la app/modulo
from .models import Producto
from django import forms

#Crear una clase por cada formulario que necesitemos
class productoForm(forms.ModelForm):
    #Definir los metadatos del form clase Meta
    class Meta:
        #Personalizar el formulario
        #1) definir el modelo
        model = Producto

        #2) definir los campos que se van a mostrar en el formulario
        fields = ['nombre', 'precio', 'imagen']

        #3) atributos de las etiquetas (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen del producto'
                }
            )
        }

        #4) personalizar las etiquetas (o los textos que salen al lado de los campos/inputs)
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen del producto'
        }

        #5) personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio',
                'unique': 'Este producto ya existe'
            },
            'precio': {
                'required': 'Este campo es obligatorio',
                'invalid': 'Ingrese un precio válido'
            },
            'imagen': {
                'required': 'Este campo es obligatorio',
                'invalid': 'Ingrese una URL válida'
            }
        }