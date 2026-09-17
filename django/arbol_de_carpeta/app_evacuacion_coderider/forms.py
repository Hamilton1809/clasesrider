from django import forms
from .models import ReporteEmergencia

class ReporteEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ReporteEmergencia
        fields = ['nombre_remitente', 'descripcion', 'foto', 'documento', 'audio', 'video']
        widgets = {
            'nombre_remitente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción de la emergencia', 'rows': 4}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'documento': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'audio': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
