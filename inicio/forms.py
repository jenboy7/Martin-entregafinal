from django import forms
from django.contrib.auth.models import User





class AlumnoFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)

class CrearAlumnoFormulario(AlumnoFormularioBase):
    ...

class EditarAlumnoFormulario(AlumnoFormularioBase):
    ...


class BuscarAlumno(forms.Form):
    apellido = forms.CharField(max_length=20, required=False)