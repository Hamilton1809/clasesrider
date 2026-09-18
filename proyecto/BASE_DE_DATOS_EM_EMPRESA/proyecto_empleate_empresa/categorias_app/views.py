from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm

def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def detalle_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'detalle_categoria.html', {'categoria': categoria})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('lista_categorias')