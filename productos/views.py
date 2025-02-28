from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets #Vamos a crear una vista de varias al mismo tiempo 
from rest_framework.renderers import JSONRenderer

class ProductoViewSet(viewsets.ModelViewSet):
    #1)Permitir saber a que objeti hago referencia
    queryset = Producto.objects.all()

    #2)Serializar los objetos
    serializer_class = ProductoSerializer

    #3)Renderizar las respuestas
    renderer_classes = [JSONRenderer] #Renderizar en formato JSON

    #4)Establecer que métodods puedo usar
    #http_method_names = ['GET', 'POST'] #Métodos permitidos