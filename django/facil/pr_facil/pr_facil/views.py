from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def bienvenida(request):
    return render(request, 'bienvenida.html')