from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', lambda request: HttpResponse("<h1>hola querido aprendices coderider esta aqui para que aprendan</h1>")),
    path('bienvenida/', lambda request: HttpResponse('bienvenidos aprendicez coderider <b>dio respuesta</b> desde el archivo <h1>urls.py de la app</h1>')),
    path('despedida/', lambda request: HttpResponse('gracias por visitarme coderider se despide')),
    path('fnrider-multilinea/', views.fnridermultilinea),
    path('fn-coderider/', views.fn_coderider),
]
