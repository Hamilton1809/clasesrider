from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_empresas, name='lista_empresas'),
    path('crear/', views.crear_empresa, name='crear_empresa'),
    path('detalle/<int:empresa_id>/', views.detalle_empresa, name='detalle_empresa'),
    path('eliminar/<int:empresa_id>/', views.eliminar_empresa, name='eliminar_empresa'),
]