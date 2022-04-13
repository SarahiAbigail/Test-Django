import django
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, "ProjectDjango1/inicio.html")

def servicios(request):
    return render(request, "ProjectDjango1/servicios.html")

def tienda(request):
    return render(request, "ProjectDjango1/tienda.html")

def blog(request):
    return render(request, "ProjectDjango1/blog.html")

def contacto(request):
    return render(request, "ProjectDjango1/contacto.html")