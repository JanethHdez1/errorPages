from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import categoriaForm

def  lista_categoria(request):
    categoria = Categoria.objects.all()

    data = [
        {
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
    

def ver_categoria(request):
    return render(request, 'ver.html') 

    