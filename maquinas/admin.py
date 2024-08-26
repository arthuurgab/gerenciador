from django.contrib import admin

from .models import Maquina
from .models import Modelos

admin.site.register(Maquina)
admin.site.register(Modelos)