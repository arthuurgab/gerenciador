from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.maquinas, name="maquina"),
    path("create/", views.createMaquina, name="createMaq"),
    path("editar/<int:id>", views.createUpdate, name="edita"),
    path("desativa/<int:id>", views.desativaMaquina, name="desativa"),
    path("deletar/", views.deletaMaquina, name="deletar")
]