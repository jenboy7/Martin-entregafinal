from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Materia
from django.urls import reverse_lazy



class Materias(ListView):
    model = Materia
    template_name = 'materias/listado_de_materias.html'
    context_object_name = 'materias'
    
    
class CrearMateria(CreateView):
    model = Materia
    template_name = 'materias/crear_materia.html'
    success_url = reverse_lazy('materias')
    fields = ['materia', 'fecha', 'descripcion' ]
    
 
class VerMateria(DetailView):
    model = Materia
    tample_name = 'materias/ver_materia.html'
    

class EditarMateria(LoginRequiredMixin, UpdateView):
    model = Materia
    template_name = 'materias/materia_update.html'
    success_url = reverse_lazy('materias')
    fields = ['materia', 'fecha', 'descripcion' ]
    
    
class EliminarMateria(LoginRequiredMixin, DeleteView):
    model = Materia
    tample_name = 'materias/materia_confirm_delete.html'
    success_url = reverse_lazy('materias')