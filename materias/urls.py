from django.urls import path
from . import views


urlpatterns = [
    path('materias/', views.Materias.as_view(), name='materias'),
    path('materias/crear/', views.CrearMateria.as_view(), name='crear_materia'),
    path('materias/<int:pk>/', views.VerMateria.as_view(), name='materia_detail'),
    path('materias/<int:pk>/editar/', views.EditarMateria.as_view(), name='materia_update'),
    path('materias/<int:pk>/eliminar/', views.EliminarMateria.as_view(), name='materia_confirm_delete')
    
    
]

