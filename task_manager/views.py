from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Proyecto, Etiqueta, Tarea
from .forms import ProyectoForm, EtiquetaForm, TareaForm, BusquedaTareaForm

def home(request):
    return render(request, 'task_manager/home.html')

def proyecto_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'task_manager/proyecto_list.html', {'proyectos': proyectos})

def proyecto_create(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'task_manager/proyecto_form.html', {'form':form})

def etiqueta_list(request):
    etiquetas = Etiqueta.objects.all()
    return render (request, 'task_manager/etiqueta_list.html', {'etiquetas': etiquetas})

def etiqueta_create(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm()
    return render(request, 'task_manager/etiqueta_form.html', {'form': form})

def tarea_list(request):
    tareas = Tarea.objects.select_related('proyecto').prefetch_related('etiquetas').all()
    return render(request, 'task_manager/tarea_list.html', {'tareas': tareas})

def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm()
    return render(request, 'task_manager/tarea_form.html', {'form': form})

def tarea_buscar(request):
    form = BusquedaTareaForm(request.GET or None)
    resultados = Tarea.objects.all()

    if form.is_valid():
        q = form.cleaned_data.get("q") or ""
        estado = form.cleaned_data.get("estado") or ""
        etiqueta = form.cleaned_data.get("etiqueta")

        filtros = Q()
        if q:
            filtros &= Q(titulo__icontains=q) | Q(descripcion__icontains=q)
        if estado:
            filtros &= Q(estado=estado)
        if etiqueta:
            filtros &= Q(etiquetas=etiqueta)

        resultados = Tarea.objects.filter(filtros).distinct()

    return render(request,"task_manager/tarea_busqueda.html",{"form": form, "tareas": resultados},)