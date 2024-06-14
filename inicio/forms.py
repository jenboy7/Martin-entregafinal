from django import forms
from django.contrib.auth.models import User





class CrearAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)