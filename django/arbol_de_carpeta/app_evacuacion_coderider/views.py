from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PuntoEvacuacion, ReporteEmergencia
from .forms import ReporteEmergenciaForm

def evacuacion_view(request):
    puntos = PuntoEvacuacion.objects.filter(estado='Activo')
    reportes = ReporteEmergencia.objects.all().order_by('-id')
    
    if request.method == 'POST':
        form = ReporteEmergenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Reporte de emergencia enviado con éxito a la central!')
            return redirect('evacuacion')
    else:
        form = ReporteEmergenciaForm()
        
    context = {
        'puntos': puntos,
        'form': form,
        'reportes': reportes,
    }
    return render(request, 'app_evacuacion_coderider/evacuacion.html', context)