from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Proyecto, Etiqueta, Tarea
from .forms import ProyectoForm, EtiquetaForm, TareaForm, BusquedaTareaForm

def home(request):
    return render(request, 'task_manager/home.html')

@login_required
def proyecto_list(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    return render(request, 'task_manager/proyecto_list.html', {'proyectos': proyectos})

@login_required
def proyecto_create(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'task_manager/proyecto_form.html', {'form':form})

@login_required
def proyecto_update(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'task_manager/proyecto_form_edit.html', {'form': form, 'proyecto': proyecto})

@login_required
def proyecto_delete(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    relacionadas = Tarea.objects.filter(usuario=request.user, proyecto=proyecto)
    if request.method == 'POST':
        if request.POST.get('delete_related') == '1':
            relacionadas.delete()
        proyecto.delete()
        return redirect('proyecto_list')
    return render(request, 'task_manager/confirm_delete.html', {
        'obj': proyecto,
        'volver_url': 'proyecto_list',
        'titulo': 'Eliminar proyecto',
        'related_count': relacionadas.count(),
    })

@login_required
def etiqueta_list(request):
    etiquetas = Etiqueta.objects.filter(usuario=request.user)
    return render (request, 'task_manager/etiqueta_list.html', {'etiquetas': etiquetas})

@login_required
def etiqueta_create(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            etiqueta = form.save(commit=False)
            etiqueta.usuario = request.user
            etiqueta.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm()
    return render(request, 'task_manager/etiqueta_form.html', {'form': form})

@login_required
def etiqueta_update(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'task_manager/etiqueta_form_edit.html', {'form': form, 'etiqueta': etiqueta})

@login_required
def etiqueta_delete(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk, usuario=request.user)
    relacionadas = Tarea.objects.filter(usuario=request.user, etiquetas=etiqueta).distinct()
    if request.method == 'POST':
        if request.POST.get('delete_related') == '1':
            relacionadas.delete()
        etiqueta.delete()
        return redirect('etiqueta_list')
    return render(request, 'task_manager/confirm_delete.html', {
        'obj': etiqueta,
        'volver_url': 'etiqueta_list',
        'titulo': 'Eliminar etiqueta',
        'related_count': relacionadas.count(),
    })

@login_required
def tarea_list(request):
    tareas = (
        Tarea.objects
        .select_related('proyecto')
        .prefetch_related('etiquetas')
        .filter(usuario=request.user)
    )
    return render(request, 'task_manager/tarea_list.html', {'tareas': tareas, 'estados': Tarea.ESTADOS})

@login_required
def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea.objects.select_related('proyecto').prefetch_related('etiquetas'), pk=pk, usuario=request.user)
    return render(request, 'task_manager/tarea_detail.html', {'tarea': tarea})

@login_required
def tarea_cambiar_estado(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        validos = dict(Tarea.ESTADOS).keys()
        if nuevo_estado in validos:
            tarea.estado = nuevo_estado
            tarea.save(update_fields=['estado'])
            messages.success(request, 'Estado actualizado')
        else:
            messages.error(request, 'Estado inválido')
    return redirect('tarea_list')

@login_required
def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST, user=request.user)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            form.save_m2m()
            return redirect('tarea_list')
    else:
        form = TareaForm(user=request.user)
    return render(request, 'task_manager/tarea_form.html', {'form': form})

@login_required
def tarea_update(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm(instance=tarea, user=request.user)
    return render(request, 'task_manager/tarea_form_edit.html', {'form': form, 'tarea': tarea})

@login_required
def tarea_delete(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tarea_list')
    return render(request, 'task_manager/confirm_delete.html', {
        'obj': tarea,
        'volver_url': 'tarea_list',
        'titulo': 'Eliminar tarea'
    })

@login_required
def tarea_buscar(request):
    form = BusquedaTareaForm(request.GET or None, user=request.user)
    resultados = Tarea.objects.filter(usuario=request.user)

    if form.is_valid():
        q = form.cleaned_data.get("q") or ""
        estado = form.cleaned_data.get("estado") or ""
        etiqueta = form.cleaned_data.get("etiqueta")
        proyecto = form.cleaned_data.get("proyecto")

        filtros = Q()
        if q:
            filtros &= Q(titulo__icontains=q) | Q(descripcion__icontains=q)
        if estado:
            filtros &= Q(estado=estado)
        if etiqueta:
            filtros &= Q(etiquetas=etiqueta)
        if proyecto:
            filtros &= Q(proyecto=proyecto)

        resultados = Tarea.objects.filter(usuario=request.user).filter(filtros).distinct()

    return render(request,"task_manager/tarea_busqueda.html",{"form": form, "tareas": resultados},)
