from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Alumno
from inicio.forms import CrearAlumnoFormulario


def inicio(request):
    return render(request, 'inicio/index.html')


def crear_alumno(request):
    
    if request.method == 'POST':
        formulario = CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
         datos = formulario.cleaned_data
         alumno = Alumno(nombre=datos.get('nombre'), apellido=datos.get('apellido'))
         alumno.save()
         return redirect('inicio') 

    formulario = CrearAlumnoFormulario()
    return render(request,r'inicio/crear_alumno.html', {'formulario':formulario})

def alumnos(request):
    
    alumnos = Alumno.objects.all()
    
    return render(request, 'inicio/alumnos.html', {'alumnos':alumnos})