from django.shortcuts import render

def index(request):
    resultado = None
    if request.method == 'POST':
        dato = request.POST.get('dato')
        resultado = f"Dato recibido por POST: <strong>{dato}</strong>"
    elif request.method == 'GET' and 'dato' in request.GET:
        dato = request.GET.get('dato')
        resultado = f"Dato recibido por GET: <strong>{dato}</strong>"

    context = {
        'resultado': resultado
    }
    return render(request, 'app_getpost_coderider/index.html', context)