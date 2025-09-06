from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Home"),
    path('add/', views.add_task, name="Add"),
    path('update_task/', views.update_task, name="upd"),
    path('delete/', views.delete_task, name="delete"),
    path('cambiar_estado/', views.cambiar_estado, name="cambiar_estado"),
]
