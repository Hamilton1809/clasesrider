from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import convocatoria

def fnridermultilinea(request):
    htmlridermultilinea = """
    <!DOCTYPE html>
    <head></head>
    <body>
    <div class="contenedor">
    <h1>¡Bienvenido a la página de FNRider Multilinea!</h1>
    <p>Esta es una página de ejemplo que muestra cómo crear una vista en Django que devuelve un contenido HTML multilinea.</p>
    <p>la funcion se llama: <strong>fnridermultilinea</strong></p>
    </div>
    </body>
    </html>
    """
    return HttpResponse(htmlridermultilinea)

def fn_coderider(request):
    return render(request, 'main_sena.html')

def crear_convocatoria(request):
    # 1. Mantenemos tu código que asegura que los registros estén en la base de datos
    convocatoria.objects.get_or_create(
        titulo_capacitacion='Capacitación en Python', 
        duracion='3 meses', 
        tipo='online',
        descripcion='Aprende Python desde cero hasta nivel avanzado.'
    )
    convocatoria.objects.get_or_create(
        titulo_capacitacion='Capacitación en Django', 
        duracion='2 meses', 
        tipo='presencial',
        descripcion='Aprende a desarrollar aplicaciones web con Django.'
    )
    convocatoria.objects.get_or_create(
        titulo_capacitacion='Capacitación en data science', 
        duracion='4 meses', 
        tipo='online',
        descripcion='Aprende a analizar datos y construir modelos predictivos.'
    )
    
    # 2. Agregamos lo necesario para consultar los datos y enviarlos a tu HTML
    todas_las_convocatorias = convocatoria.objects.all()
    
    return render(request, 'app_convocatoria/convocatoria.html', {'convocatorias': todas_las_convocatorias})
def detalles_convocatoria(request, id):
    return HttpResponse(f"Detalles de la convocatoria {id}")

def eliminar_convocatoria(request, id):
    return redirect('crear_convocatoria')