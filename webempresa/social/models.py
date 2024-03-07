from django.db import models

class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True, verbose_name='Nombre Clave') # SlugField: campo de texto que solo acepta valores alfanuméricos y guiones bajos
    name = models.CharField(max_length=100, verbose_name='Red Social')
    url = models.URLField(max_length=200, verbose_name='Enlace', null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name
