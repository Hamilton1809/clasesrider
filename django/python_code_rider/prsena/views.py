from django.shortcuts import render

def fn_inicio(request):
    return render(request, 'pr_code_sena.html')  # <-- Asegúrate de que tenga este nombre exacto