from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa, PerfilExtra
from .forms import EmpresaForm, PerfilExtraForm

def lista_empresas(request):
    # Carga rápida optimizada para obtener las 3 relaciones de un solo golpe
    empresas = Empresa.objects.select_related('categoria', 'perfil_extra').prefetch_related('beneficios')
    return render(request, 'lista_empresas.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        perfil_form = PerfilExtraForm(request.POST)
        
        if form.is_valid() and perfil_form.is_valid():
            empresa = form.save()  # Guarda empresa y la relación Muchos a Muchos (beneficios)
            
            # Guarda la relación 1 a 1 asociando la empresa creada
            perfil = perfil_form.save(commit=False)
            perfil.empresa = empresa
            perfil.save()
            
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()
        perfil_form = PerfilExtraForm()
        
    return render(request, 'crear_empresa.html', {
        'form': form, 
        'perfil_form': perfil_form
    })

def detalle_empresa(request, empresa_id):
    empresa = get_object_or_404(
        Empresa.objects.select_related('categoria', 'perfil_extra').prefetch_related('beneficios'), 
        id=empresa_id
    )
    return render(request, 'detalle_empresa.html', {'empresa': empresa})

def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    # Busca el perfil extra existente o prepara uno nuevo si no tenía
    perfil_extra, _ = PerfilExtra.objects.get_or_create(empresa=empresa)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        perfil_form = PerfilExtraForm(request.POST, instance=perfil_extra)
        
        if form.is_valid() and perfil_form.is_valid():
            form.save()
            perfil_form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm(instance=empresa)
        perfil_form = PerfilExtraForm(instance=perfil_extra)
        
    return render(request, 'editar_empresa.html', {
        'form': form, 
        'perfil_form': perfil_form, 
        'empresa': empresa
    })

def eliminar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    empresa.delete()
    return redirect('lista_empresas')