from django.contrib import admin
from django.urls import path, include
from painel import urls as painel
from maquinas import urls as maq

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(painel)),
    path("maquina/", include(maq)),
]
