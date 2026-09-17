from django.contrib import admin
from .models import PuntoEvacuacion, ReporteEmergencia

@admin.register(PuntoEvacuacion)
class PuntoEvacuacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado')

@admin.register(ReporteEmergencia)
class ReporteEmergenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_remitente', 'descripcion')
    search_fields = ('nombre_remitente', 'descripcion')