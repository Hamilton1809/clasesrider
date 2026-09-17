from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'lista_empresas.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
        Empresa.objects.create(
            nombre=request.POST.get('nombre'),
            nit=request.POST.get('nit'),
            representante=request.POST.get('representante'),
            correo=request.POST.get('correo'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion')
        )
        return redirect('lista_empresas')
    return render(request, 'crear_empresa.html')

def detalle_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    return render(request, 'detalle_empresa.html', {'empresa': empresa})

def eliminar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    empresa.delete()
    return redirect('lista_empresas')