from django.contrib import admin
from django.urls import path, include
from painel import urls as painel

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(painel)),
]
