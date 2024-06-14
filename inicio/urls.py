from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos/', views.alumnos, name="alumnos"),
    path('crear_alumno/', views.crear_alumno, name="crear_alumno")
]
