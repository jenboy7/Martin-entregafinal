from django.db import models

# Create your models here.
class Materia(models.Model):
    materia = models.CharField(max_length=20)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.materia}'
    