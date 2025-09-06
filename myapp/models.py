from django.db import models
import datetime
from django.utils import timezone


class Tareas(models.Model):
    name = models.CharField(max_length=200)
    estado = models.IntegerField(default=0)
    fecha = models.DateField(default=timezone.now)
    prioridad = models.CharField(max_length=20, default='media')
