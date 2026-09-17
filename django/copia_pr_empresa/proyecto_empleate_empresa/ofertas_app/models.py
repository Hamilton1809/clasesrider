from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.functions import Now
import uuid

# --- 1. FUNCIÓN VALIDADORA PERSONALIZADA ---
def validar_edad(value):
    """Valida que el candidato sea mayor de edad."""
    if value < 18:
        raise ValidationError("El candidato debe ser mayor de 18 años.")

# --- 2. MODELO DE CANDIDATOS ---
class Candidato(models.Model):
    # Identificadores y datos básicos
    id_candidato = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Campo de texto corto con mensajes de error personalizados
    nombre_completo = models.CharField(
        max_length=150, 
        error_messages={"blank": "El nombre es un campo obligatorio."}
    )
    
    # Entero pequeño positivo con validador y comentario en la BD
    edad = models.PositiveSmallIntegerField(
        validators=[validar_edad], 
        db_comment="Edad del usuario al registrarse"
    )
    
    # Entero pequeño estándar
    experiencia_meses = models.SmallIntegerField(
        default=0, 
        verbose_name="Meses de experiencia"
    )
    
    # Decimal de coma flotante con nombre de columna específico en la BD
    expectativa_salarial = models.FloatField(
        db_column="salario_esperado", 
        null=True, 
        blank=True
    )
    
    # Archivos multimedia
    foto = models.ImageField(upload_to='fotos_candidatos/', null=True, blank=True)
    
    # Redes e IP
    portfolio_web = models.URLField(blank=True, help_text="Enlace a LinkedIn o portafolio personal")
    ip_registro = models.GenericIPAddressField(
        null=True, 
        blank=True, 
        help_text="Dirección IPv4/IPv6 de registro"
    )
    
    # Datos estructurados JSON
    habilidades_extra = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.nombre_completo

# --- 3. MODELO DE OFERTAS DE EMPLEO ---
class OfertaEmpleo(models.Model):
    NIVELES = [
        (1, 'Junior'),
        (2, 'Semi-Senior'),
        (3, 'Senior'),
    ]

    # Campo de texto utilizado para URLs (Slug) con índice y tablespace
    slug = models.SlugField(
        max_length=100, 
        unique=True, 
        db_index=True, 
        db_tablespace="indice_slugs"
    )
    
    descripcion = models.TextField()
    
    # Campo restringido a opciones
    nivel_requerido = models.IntegerField(choices=NIVELES, default=1)
    
    # Enteros positivos
    vacantes = models.PositiveIntegerField(default=1)
    
    # Entero grande positivo, bloqueado para edición manual
    vistas_totales = models.PositiveBigIntegerField(default=0, editable=False)
    
    # Horas y Fechas
    hora_publicacion = models.TimeField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    # Estado para utilizar limit_choices_to posteriormente
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.slug

# --- 4. MODELO DE RELACIÓN (POSTULACIONES) ---
class Postulacion(models.Model):
    candidato = models.ForeignKey(
        Candidato, 
        on_delete=models.CASCADE, 
        related_name="postulaciones", 
        related_query_name="postulacion"
    )
    
    # Relación que apunta a un campo específico (to_field) y filtra por estado (limit_choices_to)
    oferta = models.ForeignKey(
        OfertaEmpleo, 
        on_delete=models.CASCADE,
        to_field="slug", 
        limit_choices_to={"activa": True},
        related_name="candidatos_inscritos"
    )
    
    # Fecha con valor por defecto directo a nivel de motor de base de datos
    fecha_aplicacion = models.DateTimeField(db_default=Now())

    class Meta:
        db_table = 'postulaciones_empleo'

    def __str__(self):
        return f"{self.candidato} -> {self.oferta.slug}"