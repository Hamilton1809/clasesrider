from django.db import models
from categorias_app.models import Categoria  # Importante: Importar el modelo de la otra app

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50, unique=True)
    representante = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    
    # Relación 1 a Muchos con null y blank permitidos
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        verbose_name="Categoría",
        related_name="empresas",
        null=True,   # Permite valores nulos en la base de datos para registros existentes
        blank=True   # Permite que el formulario o admin lo dejen en blanco si es necesario
    )
    
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nombre