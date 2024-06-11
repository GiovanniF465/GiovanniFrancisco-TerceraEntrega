from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100)

    def __str__(self):
        return f'Soy el empleado {self.nombre} {self.puesto} {self.correoElectronico}'
