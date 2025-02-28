from django.db import models

class Alumno(models.Model):
    #Atributos de la clase
    nombre = models.CharField(max_length=150) 
    apellido = models.CharField(max_length=150)
    edad = models.IntegerField()
    matricula = models.CharField(unique=True, max_length=11)
    correo = models.EmailField(unique=True, max_length=100)
    

    def __str__(self):
        return self.nombre

