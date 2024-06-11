from django.urls import path
from main import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    # path('empleados/nuevoEmpleado/<str:nombre>/<str:puesto>/<str:correoElectronico>/',views.empleadoNuevo,name="empleadoNuevo")
    path('empleados/nuevoEmpleado/',views.empleadoNuevo,name="empleadoNuevo")
]
