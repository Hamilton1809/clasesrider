from django.db import models
import uuid # Necesario para generar UUIDs

class Categoria(models.Model):
    TIPOS_OPCIONES = [
        ('Laboral', 'Laboral'),
        ('Educativa', 'Educativa'),
        ('Comercial', 'Comercial'),
        ('Otra', 'Otra'),
    ]

    # NUEVO: Reemplaza el ID clásico por un UUIDField (de tus diapositivas)
    id_categoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ACTUALIZADO: Añadimos error_messages personalizados
    nombre = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Nombre de la categoría",
        error_messages={"unique": "Ya existe una categoría con este nombre exacto."}
    )
    
    # NUEVO: SlugField ideal para generar URLs amigables
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, help_text="Texto utilizado normalmente en URLs")
    
    # ACTUALIZADO: Añadimos blank=True y help_text
    descripcion = models.TextField(
        verbose_name="Descripción",
        blank=True, 
        help_text="Proporciona una descripción detallada de esta categoría."
    )
    
    tipo_categoria = models.CharField(max_length=50, choices=TIPOS_OPCIONES, verbose_name="Tipo de categoria")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activa/Inactiva)")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # NUEVO: Se actualiza automáticamente cada vez que editas la categoría
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_categoria})"