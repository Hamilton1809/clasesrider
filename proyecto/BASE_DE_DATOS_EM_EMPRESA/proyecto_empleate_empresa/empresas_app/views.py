from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa
from .forms import EmpresaForm

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'lista_empresas.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()
    return render(request, 'crear_empresa.html', {'form': form})

def detalle_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    return render(request, 'detalle_empresa.html', {'empresa': empresa})

# <--- AQUÍ VA LA FUNCIÓN DE EDITAR
def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm(instance=empresa)
        
    return render(request, 'editar_empresa.html', {'form': form, 'empresa': empresa})

def eliminar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    empresa.delete()
    return redirect('lista_empresas')