from django.shortcuts import render
from .models import Empleado

def inicio(request):
    return render(request,'main/index.html')

def empleadoNuevo (request,nombre,puesto,correoE):
    e = Empleado(nombre=nombre,puesto=puesto,correoE=correoE)
    e.save()
    return render(request,'creacion.html',{"Empleado " : e})
