from django.db import models
from categorias_app.models import Categoria  # Importante: Importar el modelo de la otra app

# ==========================================
# 1. MODELO PARA RELACIÓN MUCHOS A MUCHOS
# ==========================================
class Beneficio(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del beneficio")
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre


# ==========================================
# MODELO PRINCIPAL: EMPRESA
# ==========================================
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50, unique=True)
    representante = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    
    # ------------------------------------------
    # RELACIÓN 1 A MUCHOS (La que ya tenías)
    # ------------------------------------------
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        verbose_name="Categoría",
        related_name="empresas",
        null=True,  
        blank=True  
    )
    
    # ------------------------------------------
    # RELACIÓN MUCHOS A MUCHOS (Nueva)
    # ------------------------------------------
    # Una empresa ofrece muchos beneficios (ej: Trabajo remoto, Seguro médico) 
    # y un beneficio es ofrecido por muchas empresas.
    beneficios = models.ManyToManyField(
        Beneficio,
        blank=True,
        verbose_name="Beneficios ofrecidos"
    )
    
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nombre


# ==========================================
# 3. MODELO PARA RELACIÓN 1 A 1
# ==========================================
class PerfilExtra(models.Model):
    # Un perfil pertenece exclusivamente a una sola empresa, 
    # y una empresa tiene un solo perfil extra.
    empresa = models.OneToOneField(
        Empresa, 
        on_delete=models.CASCADE, 
        related_name="perfil_extra",
        verbose_name="Empresa"
    )
    sitio_web = models.URLField(max_length=200, blank=True, null=True, verbose_name="Página Web")
    link_linkedin = models.URLField(max_length=200, blank=True, null=True, verbose_name="Perfil de LinkedIn")
    descripcion_larga = models.TextField(blank=True, null=True, verbose_name="Historia / Misión de la empresa")

    def __str__(self):
        return f"Perfil de: {self.empresa.nombre}"