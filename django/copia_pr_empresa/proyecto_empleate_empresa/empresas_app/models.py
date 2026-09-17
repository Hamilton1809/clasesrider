from django.db import models
import uuid
# Importamos Categoria para poder relacionarlas
from categorias_app.models import Categoria 

class Empresa(models.Model):
    # NUEVO: UUIDField
    id_empresa = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ACTUALIZADO: Añadimos db_column y db_index
    nombre = models.CharField(
        max_length=200, 
        db_column="nombre_completo", 
        db_index=True
    )
    nit = models.CharField(max_length=50, unique=True)
    representante = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    # --- NUEVOS CAMPOS SEGÚN TUS DIAPOSITIVAS ---

    # Relación Foránea: limit_choices_to asegura que solo se elijan categorías donde estado=True
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        limit_choices_to={'estado': True},
        verbose_name="Categoría de la Empresa"
    )

    # Subida de archivos (Requiere instalar Pillow)
    logo = models.ImageField(upload_to='logos_empresas/', null=True, blank=True)
    
    # URL de la empresa
    sitio_web = models.URLField(null=True, blank=True)
    
    # Entero positivo con comentario directo en el motor de base de datos
    numero_empleados = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        db_comment="Cantidad total de empleados activos en la empresa"
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nombre