from django import forms

class BaseEmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    puesto = forms.CharField(max_length=100)
    correoElectronico = forms.CharField(max_length=100)
    
class crearEmpleadoFormulario(BaseEmpleadoFormulario):
    ...

class editarEmpleadoFormulario(BaseEmpleadoFormulario):
    ...

class buscarEmpleado(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)