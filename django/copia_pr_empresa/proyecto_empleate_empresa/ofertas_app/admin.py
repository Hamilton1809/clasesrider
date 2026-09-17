from django.contrib import admin
from .models import Candidato, OfertaEmpleo, Postulacion

admin.site.register(Candidato)
admin.site.register(OfertaEmpleo)
admin.site.register(Postulacion)