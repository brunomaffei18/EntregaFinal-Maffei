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
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['proyecto'].queryset = Proyecto.objects.filter(usuario=user)
            self.fields['etiquetas'].queryset = Etiqueta.objects.filter(usuario=user)
    
class BusquedaTareaForm(forms.Form):
    q = forms.CharField(label='Buscar por título', required=False)
    estado = forms.ChoiceField(choices=[('', '---')] + Tarea.ESTADOS, required=False)
    proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.none(), required=False)
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.none(), required=False)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['proyecto'].queryset = Proyecto.objects.filter(usuario=user)
            self.fields['etiqueta'].queryset = Etiqueta.objects.filter(usuario=user)
