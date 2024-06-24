from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Alumno
from inicio.forms import AlumnoFormularioBase, CrearAlumnoFormulario,EditarAlumnoFormulario, BuscarAlumno


def inicio(request):
    return render(request, 'inicio/index.html')


def crear_alumno(request):
    formulario = CrearAlumnoFormulario()
    
    if request.method == 'POST':
        formulario = CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
         datos = formulario.cleaned_data
         alumno = Alumno(nombre=datos.get('nombre'), apellido=datos.get('apellido'))
         alumno.save()
         return redirect('inicio') 

    
    return render(request,r'inicio/crear_alumno.html', {'formulario':formulario})

def alumnos(request):
    
    formulario = BuscarAlumno(request.GET)
    if formulario.is_valid():
        apellido = formulario.cleaned_data['apellido']
        alumnos = Alumno.objects.filter(apellido__icontains=apellido)
    
    # alumnos = Alumno.objects.all()
    
    return render(request, 'inicio/alumnos.html', {'alumnos':alumnos, 'formulario': formulario})

def eliminar_alumno (request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    
    formulario = EditarAlumnoFormulario(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido})
    
    if request.method == 'POST':
        formulario = EditarAlumnoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            alumno.nombre = info['nombre']
            alumno.apellido = info['apellido']
            alumno.save()
            return redirect('alumnos')
    
    
    return render(request, 'inicio/editar_alumno.html', {'formulario': formulario, 'alumno': alumno})

def ver_alumno(request, id):
        alumno = Alumno.objects.get(id=id)
        return render(request, 'inicio/ver_alumno.html', {'alumno': alumno})