from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from tkinter import image_names
from django.db import models
from django.forms import CharField

# Create your models here.

#se crearán los modelos necesarios para la BD
class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios' 
        
def __str__(self):
    return self.titulo