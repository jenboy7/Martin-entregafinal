from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
