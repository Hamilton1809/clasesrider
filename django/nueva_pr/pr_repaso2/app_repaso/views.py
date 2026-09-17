from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MiCurso

def bienvenida_app(request):
    cursos = MiCurso.objects.all()
    return render(request, 'app-repaso/app_bienvenida.html', {'cursos': cursos})

def crear_curso(request):
    return HttpResponse("Página para crear un nuevo curso")

def detalle_curso(request, curso_id):
    curso = get_object_or_404(MiCurso, id=curso_id)
    return render(request, 'app-repaso/app_detalle.html', {'curso': curso})

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(MiCurso, id=curso_id)
    curso.delete()
    return redirect('bienvenida_app')