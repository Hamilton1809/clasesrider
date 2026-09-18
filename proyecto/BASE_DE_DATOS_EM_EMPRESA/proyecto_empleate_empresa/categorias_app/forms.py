from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'tipo_categoria', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Tecnología e Informática'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción de la categoría...'}),
            'tipo_categoria': forms.Select(),
            'estado': forms.CheckboxInput(),
        }