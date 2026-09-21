from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('crear/', views.crear_categoria, name='crear_categoria'),
    path('<int:id>/', views.detalle_categoria, name='detalle_categoria'),
    path('eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
]