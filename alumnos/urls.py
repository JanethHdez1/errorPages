from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
#registrar el path común para las rutas
router.register(r'api',AlumnoViewSet)

urlpatterns = [
    path('agregar/', AlumnoTemplateView.as_view(), name='agregar'),
    path('', include(router.urls)),   
]