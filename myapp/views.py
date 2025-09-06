from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas
from django.http import JsonResponse
# Create your views here.


def index(request):
    tareas = Tareas.objects.all()

    if request.method == "GET":
        mostrar = request.GET.get('mostrar')
        if mostrar is None:
            mostrar = 'verTodo'

        if mostrar == 'verTodo':
            tareas = Tareas.objects.all()
        else:
            mostrar = int(mostrar)

        if mostrar == 0:
            tareas = Tareas.objects.filter(estado=0)
        elif mostrar == 1:
            tareas = Tareas.objects.filter(estado=1)

        prioridad = request.GET.get('verPrioridad')

        if prioridad == 'Alta':
            tareas = Tareas.objects.filter(prioridad='Alta')
        elif prioridad == 'Media':
            tareas = Tareas.objects.filter(prioridad='Media')
        elif prioridad == 'Baja':
            tareas = Tareas.objects.filter(prioridad='Baja')

    return render(request, "home.html", {'lista': tareas})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        prioridad = request.POST.get('prioridad')

        if title and status and prioridad:
            tarea = Tareas(
                name=title,
                estado=int(status),
                prioridad=prioridad
            )
    tarea.save()

    return redirect("/")


def update_task(request):
    idupd = request.POST.get('update')
    tarea = get_object_or_404(Tareas, id=idupd)

    if request.method == "POST":
        tarea.name = request.POST.get('title', tarea.name)
        tarea.prioridad = request.POST.get('prioridad', tarea.prioridad)
        tarea.save()

        return redirect("/")


def delete_task(request):
    id = request.POST.get('delete')
    tarea = get_object_or_404(Tareas, id=id)
    tarea.delete()

    return redirect("/")


def cambiar_estado(request):
    if request.method == "POST":
        tarea_id = request.POST.get('check')
        last_estado = int(request.POST.get('lastEstado'))

        tarea = get_object_or_404(Tareas, id=tarea_id)

        if last_estado == 0:
            tarea.estado = 1
            tarea.save()
        else:
            tarea.estado = 0
            tarea.save()

    return JsonResponse({
        'status': 'ok',
        'id': tarea.id,
        'estado': tarea.estado,
    })
