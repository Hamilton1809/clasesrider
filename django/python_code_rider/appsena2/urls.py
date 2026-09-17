from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_appsena2, name='hola_appsena2'),
]