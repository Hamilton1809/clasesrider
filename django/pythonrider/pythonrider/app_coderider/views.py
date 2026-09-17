from django.shortcuts import render
from django.http import HttpResponse
def fnridermultilinea(request):
    htmlridermultilinea = """
    <!DOCTYPE html>
    <head></head>
    <body>
        <div class="contenedor">
            <h1> Hola Rider </h1>
            <p>
            contenido almacenado en variable python con miltilinea . 
            </p>
            <p>
            la funcion se llama:
            <strong>fnridermultilinea</strong>
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(htmlridermultilinea)


def fn_coderider(request):
    return render(request, 'main_code_rider.html')

# Create your views here.
