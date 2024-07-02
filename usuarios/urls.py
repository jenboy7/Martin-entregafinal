from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import perfil
from .views import CambiarPassword

urlpatterns = [
    path('login/', views.login, name='login' ),
    path('logout/', LogoutView.as_view(template_name = 'usuario/logout.html') , name='logout'),
    path('registro/', views.registro , name='registro'),
    path('perfil_edit/', views.perfil_edit , name='perfil_edit'),
    path('perfil/<int:id>', perfil, name='perfil'),
    path('perfil/perfil_edit/password/', views.CambiarPassword.as_view() , name='cambiarpass'),
    
    ]

