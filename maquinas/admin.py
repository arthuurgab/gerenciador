from django.contrib import admin

from .models import Maquina
from .models import Especificacoes

admin.site.register(Maquina)
admin.site.register(Especificacoes)
