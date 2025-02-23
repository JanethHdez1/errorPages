from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import categoriaForm
import json


def  lista_categoria(request):
    categoria = Categoria.objects.all()

    data = [
        {
            'id': c.id,
            'nombre': c.nombre,
            'imagen': c.imagen,
        }
        for c in categoria
    ]

    return JsonResponse(data, safe=False)


def registrar_categoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('json') 
        
    else:
        form = categoriaForm()
    return render(request, 'registrar.html', {'form': form})


def agregar_categoria(request):
    #checar si nuestra request es de tipo POST
    if request.method == 'POST':
        #quiere decir que si estoy manejando el request
        try:
            data=json.loads(request.body) #parametro es un texto que deberia ser un JSON
            #creo un nuevo categoria
            categoria=Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            ) #create directamente mete el objeto en la BD
            #devolver un mensaje de exito
            return JsonResponse(
                {
                'mensaje':'Registro exitoso',
                'id':categoria.id,
                },status=201)
        except Exception as e:
            return JsonResponse({'error':str(e),},status=400)
    return JsonResponse({'error': 'Método no soportado'}, status=405)


def ver_categoria(request):
    return render(request, 'ver.html') 