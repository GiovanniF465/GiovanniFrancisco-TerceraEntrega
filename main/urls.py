from django.urls import path
from main import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('empleados/nuevoEmpleado/',views.empleadoNuevo,name="empleadoNuevo"),
    path('empleados/',views.empleados,name="empleadosV"),
    path('empleados/eliminarEmpleado/<int:id>',views.eliminarEmpleado,name="eliminarEmpleado"),
    path('empleado/editarEmpleado/<int:id>',views.editarEmpleado,name="editarEmpleado"),
]
