from .models import Alumno
from .forms import AlumnoForm
from .serializers import AlumnoSerializer
from rest_framework import viewsets  # Vamos a crear una vista de varias al mismo tiempo
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, redirect
from django.views import View


class AlumnoViewSet(viewsets.ModelViewSet):
    # 1) Permitir saber a qué objeto hago referencia
    queryset = Alumno.objects.all()

    # 2) Serializar los objetos
    serializer_class = AlumnoSerializer

    # 3) Renderizar las respuestas
    renderer_classes = [JSONRenderer]  # Renderizar en formato JSON

    # 4) Establecer qué métodos puedo usar
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos permitidos


class AlumnoTemplateView(View):
    def get(self, request):
        return render(request, 'Hernandez_Janeth.html')