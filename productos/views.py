from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import productoForm

#método que devuelve el JSON - que es una vista
def  lista_productos(request):
    #Obtener todas las instancias de la clase Producto
    productos = Producto.objects.all()

    #Construir una variable en formato diccionario, porque es la estructura que se necesita para devolver un JSON
    data = [
        {
            #Objeto Producto construido al aire
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen,
        }
        for p in productos
    ]

    #Devolver la respuesta en JSON
    return JsonResponse(data, safe=False)

#Función para mandar a la vista del formulario
def agregar_producto(request):
    #Averiguar si estamos teniendo una respuesta de form
    if request.method == 'POST':
        #Crear un objeto de tipo productoForm
        form = productoForm(request.POST)

        if form.is_valid():
            form.save() #Guardar el objeto en la base de datos
            return redirect('agregar') #Redirigir a la lista de productos
        
        #Pintar el formulario en la vista
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form': form})

    