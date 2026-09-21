from django import forms
from .models import Empresa, PerfilExtra

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
            'categoria',   # Relación 1 a Muchos
            'beneficios',  # Relación Muchos a Muchos
        ]
        widgets = {
            'beneficios': forms.CheckboxSelectMultiple(), # Muestra los beneficios como casillas seleccionables
        }

class PerfilExtraForm(forms.ModelForm):
    class Meta:
        model = PerfilExtra
        fields = ['sitio_web', 'link_linkedin', 'descripcion_larga']