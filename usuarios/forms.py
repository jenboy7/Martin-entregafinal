from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class NuestroFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repertir contraseña", widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {key:'' for key in fields}
        

class PerfilEdit(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombres')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']





