from django.shortcuts import render
from main.models import Empleado
from main.forms import crearEmpleadoFormulario

def inicio(request):
    return render(request,'main/index.html')

# def empleadoNuevo (request,nombre,puesto,correoElectronico):
#     empleado = Empleado(nombre=nombre,puesto=puesto,correoElectronico=correoElectronico)
#     empleado.save()
#     return render(request,'creacion.html',{'Empleado': empleado})

def empleadoNuevo (request):
    print(request)
    print(request.GET)
    print(request.POST)
    
    #request.POST
    if request.method == 'POST':
        formulario = crearEmpleadoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            empleado = Empleado(nombre=datos.get('nombre'),puesto=datos.get('puesto'),correoElectronico=datos.get('correoElectronico'))
            empleado.save()
    formulario = crearEmpleadoFormulario()
    
    return render(request,'creacion.html', {'formulario': formulario})
