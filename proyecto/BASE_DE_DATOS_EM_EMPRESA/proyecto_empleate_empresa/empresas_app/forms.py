from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre', 
            'nit', 
            'representante', 
            'correo', 
            'telefono', 
            'direccion', 
            'categoria'  # <--- Agregado para que se muestre en el formulario
        ]