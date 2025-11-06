from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='proyectos')

    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='etiquetas')

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    ESTADOS = [
        ('toDo', 'Pendiente'),
        ('doing', 'En progreso'),
        ('done', 'Finalizado')
    ]
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='toDo')
    fecha_limite = models.DateField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='tareas')
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tareas')

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"
