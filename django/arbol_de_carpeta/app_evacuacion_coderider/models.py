from django.db import models

class PuntoEvacuacion(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    capacidad = models.IntegerField(default=100)
    estado = models.CharField(max_length=50, default='Activo')

    def __str__(self):
        return self.nombre

class ReporteEmergencia(models.Model):
    TIPO_CHOICES = [
        ('Sismo', 'Sismo'),
        ('Incendio', 'Incendio'),
        ('Inundacion', 'Inundación'),
        ('Otro', 'Otro'),
    ]
    nombre_remitente = models.CharField(max_length=100, verbose_name="Nombre Completo")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción Adicional") 
    foto = models.ImageField(upload_to='fotos_emergencias/', blank=True, null=True, verbose_name="Foto de la Emergencia")
    documento = models.FileField(upload_to='documentos_emergencias/', blank=True, null=True, verbose_name="Documento de la Emergencia")
    audio = models.FileField(upload_to='audios_emergencias/', blank=True, null=True, verbose_name="Audio de la Emergencia")
    fecha = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos_emergencias/', blank=True, null=True, verbose_name="Video de la Emergencia")

    def __str__(self):
        return f"{self.tipo_emergencia} - {self.nombre_remitente}"
