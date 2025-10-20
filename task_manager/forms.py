from django import forms
from .models import Proyecto, Etiqueta, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado', 'fecha_limite', 'proyecto', 'etiquetas']
    
class BusquedaTareaForm(forms.Form):
    q = forms.CharField(label='Buscar por título', required=False)
    estado = forms.ChoiceField(choices=[('', '---')] + Tarea.ESTADOS, required=False)
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.all(), required=False)