import django
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Inicio")

def servicios(request):
    return HttpResponse("Sevicios")

def tienda(request):
    return HttpResponse("Tienda")

def blog(request):
    return HttpResponse("Blog")

def contacto(request):
    return HttpResponse("contacto")