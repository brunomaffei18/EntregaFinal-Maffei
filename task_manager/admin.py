from django.contrib import admin

# Register your models here.
from .models import Proyecto, Etiqueta, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado')

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'estado', 'fecha_limite', 'creado')
    list_filter = ('estado', 'proyecto', 'etiquetas')
    search_fields = ('titulo', 'descripcion')