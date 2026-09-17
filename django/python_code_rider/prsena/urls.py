from django.contrib import admin
from django.urls import path, include

from prsena import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fn_inicio, name='inicio'),  # Ruta para la vista de inicio
    path('appsena/appsena2/', include('appsena2.urls')), # Carga la respuesta de appsena2
    path('appsena/', include('appsena.urls')),           # Carga todo lo de appsena (incluyendo appsena3/)
]