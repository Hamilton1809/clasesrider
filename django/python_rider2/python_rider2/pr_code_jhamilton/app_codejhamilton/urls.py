from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("<h1>hola querido aprendices codejhamilton esta aqui para que aprendan</h1>")),
    path('bienvenida/', lambda request: HttpResponse('bienvenidos aprendicez codejhamilton <b>dio respuesta</b> desde el archivo <h1>urls.py de la app</h1>')),
    path('despedida/', lambda request: HttpResponse('gracias por visitarme codejhamilton se despide')),
]