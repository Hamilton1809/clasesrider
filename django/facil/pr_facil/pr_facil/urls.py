from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                     # http://127.0.0.1:8000/ -> Evaluación
    path('popayan/', views.bienvenida, name='bienvenida'), # http://127.0.0.1:8000/popayan/ -> Bienvenida (desde PR)
    path('popayan/', include('app_facil.urls')),          # Maneja las vistas de app_facil
]