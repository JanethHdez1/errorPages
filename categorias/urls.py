from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_categoria, name='lista'),
    path('registrar/', registrar_categoria, name='registrar'),
    path ('api/post/', agregar_categoria, name='agregar'),
    path('json/', ver_categoria, name='json'),
]