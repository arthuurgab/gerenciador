from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.maquinas, name="maquina"),
    path("create/", views.createMaquina, name="createMaq"),
]