from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Proyectos
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/nuevo/', views.proyecto_create, name='proyecto_create'),

    # Etiquetas
    path('etiquetas/', views.etiqueta_list, name='etiqueta_list'),
    path('etiquetas/nueva/', views.etiqueta_create, name='etiqueta_create'),

    # Tareas
    path('tareas/', views.tarea_list, name='tarea_list'),
    path('tareas/nueva/', views.tarea_create, name='tarea_create'),

    # Búsqueda
    path('tareas/buscar/', views.tarea_buscar, name='tarea_buscar'),
]