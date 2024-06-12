from django.shortcuts import render,redirect
from main.models import Empleado
from main.forms import crearEmpleadoFormulario,buscarEmpleado,editarEmpleadoFormulario

def inicio(request):
    return render(request,'main/index.html')

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
            return redirect('empleados')
    formulario = crearEmpleadoFormulario()
    
    return render(request,'creacion.html', {'formulario': formulario})

def empleados(request):
    formulario = buscarEmpleado(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        empleados = Empleado.objects.filter(nombre__icontains=nombre)
        
    
  #  empleados = Empleado.objects.all()
    
    return render(request,'empleados.html', {'empleados':empleados,'formulario': formulario})

def eliminarEmpleado(request,id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleadosV')

def editarEmpleado(request,id):
    empleado = Empleado.objects.get(id=id)
    formulario = editarEmpleadoFormulario(initial={'nombre': empleado.nombre,'puesto': empleado.puesto,'correoElectronico':empleado.correoElectronico})
    
    if request.method == 'POST':
        formulario = editarEmpleadoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            empleado.nombre = info['nombre']
            empleado.puesto = info['puesto']
            empleado.correoElectronico = info['correoElectronico']
            empleado.save()
            return redirect('empleadosV')
    
    return render(request,'editarEmpleado.html',{'formulario':formulario,'empleado':empleado})