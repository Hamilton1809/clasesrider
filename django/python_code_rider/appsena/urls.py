from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render  # <-- 1. Importa 'render' aquí
from appsena import views
from . import views

urlpatterns = [
    path('', lambda request: HttpResponse('<h1><b>edwin se la come entera!</b></h1>')),
    path('bienvenido/', lambda request: HttpResponse('<h1><b>¡Bienvenido a la aplicación!</b></h1>')),
    path('despedida/', lambda request: HttpResponse('<h1><b>¡Hasta luego! ¡Gracias por visitar nuestra aplicación!</b></h1>')),
    path('fnrider-multilinea/', views.fnridermultilinea),
    path('fn-coderider/', views.fn_coderider),
    path('appsena3/', lambda request: render(request, 'main.sena2.html')),
    path('crear_convocatoria/', views.crear_convocatoria, name='crear_convocatoria'),
    
    # Nuevas rutas agregadas:
    path('detalles/<int:id>/', views.detalles_convocatoria, name='detalles_convocatoria'),
    path('eliminar/<int:id>/', views.eliminar_convocatoria, name='eliminar_convocatoria'),
]