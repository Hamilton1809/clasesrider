from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta para el módulo de empresas
    path('empresas/', include('empresas_app.urls')), 
    # Ruta para el módulo de categorías
    path('categorias/', include('categorias_app.urls')), 
]