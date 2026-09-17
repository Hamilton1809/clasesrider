from django.shortcuts import render
from django.db.models import Q
from .models import Temblor

def procesar_busqueda_url(request):
    """Procesa búsquedas que vienen en la URL con signos de interrogación (?)"""
    temblores = Temblor.objects.all()
    filtros_texto = []

    # Capturar parámetros de la URL
    id_val = request.GET.get('id')
    lugar_val = request.GET.get('ciudad') or request.GET.get('lugar')
    magnitud_val = request.GET.get('magnitud')
    rango_val = request.GET.get('rango')
    area_val = request.GET.get('area')
    profundidad_val = request.GET.get('profundidad')
    fecha_val = request.GET.get('fecha')
    hora_val = request.GET.get('hora')

    if id_val:
        temblores = temblores.filter(id=id_val)
        filtros_texto.append(f"ID={id_val}")

    if lugar_val:
        temblores = temblores.filter(lugar__icontains=lugar_val)
        filtros_texto.append(f"Ciudad/Lugar={lugar_val}")

    if magnitud_val:
        temblores = temblores.filter(magnitud=magnitud_val)
        filtros_texto.append(f"Magnitud={magnitud_val}")

    if rango_val:
        temblores = temblores.filter(rango__icontains=rango_val)
        filtros_texto.append(f"Rango={rango_val}")

    if area_val:
        temblores = temblores.filter(area__icontains=area_val)
        filtros_texto.append(f"Área={area_val}")

    if profundidad_val:
        temblores = temblores.filter(profundidad__icontains=profundidad_val)
        filtros_texto.append(f"Profundidad={profundidad_val}")

    if fecha_val:
        try:
            temblores = temblores.filter(fecha__icontains=fecha_val)
        except Exception:
            temblores = temblores.filter(fecha=fecha_val)
        filtros_texto.append(f"Fecha={fecha_val}")

    if hora_val:
        try:
            temblores = temblores.filter(hora__icontains=hora_val)
        except Exception:
            temblores = temblores.filter(hora=hora_val)
        filtros_texto.append(f"Hora={hora_val}")

    query_str = ", ".join(filtros_texto) if filtros_texto else "Búsqueda vía URL"

    return render(request, 'salida-temblor.html', {
        'temblores': temblores.order_by('-id'),
        'modo': 'buscar',
        'query': query_str
    })


def temblor_view(request):
    # Si ingresan datos en la URL mediante GET (ej. ?fecha=2024-05-20&hora=14:30)
    if request.GET:
        return procesar_busqueda_url(request)

    return render(request, 'temblor.html')


def salida_temblor_view(request):
    if request.method == 'GET' and request.GET:
        return procesar_busqueda_url(request)

    if request.method == 'POST':
        action = request.POST.get('action')

        # 1. Guardar registro
        if action == 'enviar':
            temblor_guardado = Temblor.objects.create(
                magnitud=request.POST.get('magnitud'),
                profundidad=request.POST.get('profundidad'),
                rango=request.POST.get('rango'),
                lugar=request.POST.get('lugar'),
                area=request.POST.get('area'),
                fecha=request.POST.get('fecha'),
                hora=request.POST.get('hora')
            )
            return render(request, 'salida-temblor.html', {
                'temblor': temblor_guardado,
                'modo': 'ultimo'
            })

        # 2. Listar todos
        elif action == 'listar':
            temblores = Temblor.objects.all().order_by('-id')
            return render(request, 'salida-temblor.html', {
                'temblores': temblores,
                'modo': 'todos'
            })

        # 3. Buscar mediante el formulario
        elif action == 'buscar':
            query = request.POST.get('query', '').strip()

            filtros = (
                Q(lugar__icontains=query) | 
                Q(rango__icontains=query) | 
                Q(area__icontains=query) | 
                Q(profundidad__icontains=query) |
                Q(fecha__icontains=query) |
                Q(hora__icontains=query)
            )

            if query.isdigit():
                filtros |= Q(id=int(query))

            try:
                filtros |= Q(magnitud=float(query))
            except ValueError:
                pass

            temblores = Temblor.objects.filter(filtros).distinct().order_by('-id')
            return render(request, 'salida-temblor.html', {
                'temblores': temblores,
                'modo': 'buscar',
                'query': query
            })

    temblores = Temblor.objects.all().order_by('-id')
    return render(request, 'salida-temblor.html', {'temblores': temblores, 'modo': 'todos'})