from django import forms

class crearEmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    puesto = forms.CharField(max_length=100)
    correoElectronico = forms.CharField(max_length=100)

