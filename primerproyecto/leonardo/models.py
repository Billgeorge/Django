# coding=utf-8
from django.db import models


class Leonardo(models.Model):
	edad = models.IntegerField()
	nombre_completo= models.CharField(max_length=200)
	correo= models.CharField(max_length=200)
	descripcion= models.TextField()
	numero_celular=models.IntegerField()
	descripcion_corta=models.TextField(default="Descripcion Corta")
	
	
	def __str__(self):
		return self.nombre_completo
	
	
# Create your models here.
