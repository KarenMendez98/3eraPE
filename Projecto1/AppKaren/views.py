from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppKaren/inicio.html")
