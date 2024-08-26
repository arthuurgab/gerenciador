from django.db import models
from maquinas.models import Maquina

class Equipamentos(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    apelido = models.CharField(max_length=250, blank=False, help_text="Define o Apelido (Nome) do Equipamento")
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    numeroSerie = models.CharField(max_length=10, unique=True, null=False, help_text="Define o Número de Série do Equipamento")

    # Especificações do Equipamento
    altura = models.FloatField(null=True, help_text="Define a Altura do Equipamento")
    largura = models.FloatField(null=True, help_text="Define a Largura do Equipamento")
    comprimento = models.FloatField(null=True, help_text="Define o Comprimento do Equipamento")

    def __str__(self):
        return str(f"{self.apelido} - {self.maquina}")