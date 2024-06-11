from django.urls import path
from main import views

urlpatterns = [
    path('',views.inicio),
    path('empleados/nuevoEmpleado/',views.empleadoNuevo)
]
