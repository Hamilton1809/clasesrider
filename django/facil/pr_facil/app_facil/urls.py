from django.urls import path
from . import views

urlpatterns = [
    path('temblor/', views.temblor_view, name='temblor'),
    path('saida-temblor/', views.salida_temblor_view, name='salida_temblor'),
]