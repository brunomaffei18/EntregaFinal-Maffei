from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Proyectos
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/nuevo/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', views.proyecto_delete, name='proyecto_delete'),

    # Etiquetas
    path('etiquetas/', views.etiqueta_list, name='etiqueta_list'),
    path('etiquetas/nueva/', views.etiqueta_create, name='etiqueta_create'),
    path('etiquetas/<int:pk>/editar/', views.etiqueta_update, name='etiqueta_update'),
    path('etiquetas/<int:pk>/eliminar/', views.etiqueta_delete, name='etiqueta_delete'),

    # Tareas
    path('tareas/', views.tarea_list, name='tarea_list'),
    path('tareas/<int:pk>/', views.tarea_detail, name='tarea_detail'),
    path('tareas/<int:pk>/estado/', views.tarea_cambiar_estado, name='tarea_cambiar_estado'),
    path('tareas/nueva/', views.tarea_create, name='tarea_create'),
    path('tareas/<int:pk>/editar/', views.tarea_update, name='tarea_update'),
    path('tareas/<int:pk>/eliminar/', views.tarea_delete, name='tarea_delete'),

    # Búsqueda
    path('tareas/buscar/', views.tarea_buscar, name='tarea_buscar'),
]
