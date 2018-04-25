from django.db import models

# Create your models here.

class Persona(models.Model):
	#persona = models.ForeingKey(Persona, null = True, blank = True, on_delete = models.CASCADE)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()
