from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida_app, name='bienvenida_app'),
    path('crear/', views.crear_curso, name='crear_curso'),
    # Agrega estas dos líneas:
    path('detalle/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
]