from django.urls import path
from . import views


urlpatterns = [
    path('materias/', views.Materias.as_view(), name='materias'),
    path('materias/crear/', views.CrearMateria.as_view(), name='crear_materia'),
    path('materias/<int:pk>/', views.VerMateria.as_view(), name='ver_materia')
    
    
]

