from django.db import models

class convocatoria(models.Model):
    titulo_capacitacion = models.CharField(max_length=255)
    duracion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    detalle = models.TextField()
    descripcion = models.CharField(max_length=255, blank=True, null=True)