from django.http import HttpResponse

def hola_appsena2(request):
    return HttpResponse("<h1>¡Hola! Este mensaje viene directo desde el views.py de Appsena 2 </h1>")