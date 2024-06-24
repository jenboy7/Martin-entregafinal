from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_alumno/', views.crear_alumno, name="crear_alumno"),
    path('alumnos/', views.alumnos, name="alumnos"),
    path('alumnos/eliminar/<int:id>', views.eliminar_alumno, name="eliminar_alumno"),
    path('alumnos/editar/<int:id>', views.editar_alumno, name="editar_alumno"),
    path('alumnos/editar/<int:id>', views.editar_alumno, name="editar_alumno"),
    path('alumnos/<int:id>', views.ver_alumno, name="ver_alumno"),
    
    
]
