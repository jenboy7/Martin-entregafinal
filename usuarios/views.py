from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import NuestroFormularioDeCreacion, PerfilEdit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra
from django.contrib.auth.models import User


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            
            user = authenticate(username=username, password=password)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=user)
            
            return redirect('inicio')
        
    return render(request, 'usuario/login.html', {'formulario': formulario})


def registro(request):
    
    formulario = NuestroFormularioDeCreacion()
    
    if request.method == "POST":
        formulario = NuestroFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    
    return render(request, "usuario/registro.html", {'formulario' : formulario})

@login_required
def perfil(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'usuario/perfil.html', {'user': user})


@login_required
def perfil_edit(request):
    
    datosextra =  request.user.datosextra
    
    formulario = PerfilEdit(initial={'avatar': datosextra.avatar},instance=request.user)
    
    if request.method == "POST":
        formulario = PerfilEdit(request.POST, request.FILES , instance=request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            
            datosextra.avatar = avatar
            datosextra.save()
            
            formulario.save()
            return redirect('perfil_edit')
        
    return render(request, 'usuario/perfil_edit.html', {'formulario': formulario})


class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/cambiarpass.html'
    success_url = reverse_lazy('perfil_edit')