from django.db import models

class Categoria(models.Model):
    TIPOS_OPCIONES = [
        ('Laboral', 'Laboral'),
        ('Educativa', 'Educativa'),
        ('Comercial', 'Comercial'),
        ('Otra', 'Otra'),
    ]

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(verbose_name="Descripción")
    tipo_categoria = models.CharField(max_length=50, choices=TIPOS_OPCIONES, verbose_name="Tipo de categoría")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activa/Inactiva)")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_categoria})"