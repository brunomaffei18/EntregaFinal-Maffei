from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    ESTADOS = [
        ('toDo', 'Por hacer'),
        ('doing', 'En progreso'),
        ('done', 'Hecha')
    ]
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='toDo')
    fecha_limite = models.DateField(null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='tareas')
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"