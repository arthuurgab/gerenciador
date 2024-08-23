from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.painel, name="painel")
]