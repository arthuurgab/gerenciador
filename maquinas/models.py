from django.db import models
from modelos.models import models, Modelos

class Maquina(models.Model):
    STATUS_CHOICES = (
        (0, 'Inativo'),
        (1, 'Ativo'),
    )

    # Define a Tensão de Entrada da Máquina
    POWER_CHOICES = (
        (480, '480Vac'),
        (460, '460Vac'),
        (440, '440Vac'),
        (415, '415Vac'),
        (400, '400Vac'),
        (380, '380Vac'),
        (240, '240Vac'),
        (220, '220Vac'),
        (208, '208Vac'),
    )

    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    apelido = models.CharField(max_length=250, blank=False, help_text="Define o Apelido (Nome) da Máquina")
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE, help_text="Define o Modelo da Máquina")
    dataFabricacao = models.DateField(null=False, blank=False, help_text="Define o Data da Fabricação da Máquina")
    numeroSerie = models.CharField(max_length=10, unique=True, null=False, help_text="Define o Número de Série da Máquina")
    dataStartup = models.DateField(null=False, blank=False, help_text="Define o Data da Instalação da Máquina")
    custo = models.FloatField(null=False, blank=True, help_text="Define o Custo da Máquina")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, help_text="Define o Status da Máquina, por Padrão Ativa (1)")

    # Especificações
    inputPower = models.IntegerField(choices=POWER_CHOICES, null=False, help_text="Define a Tensão de Entrada da Máquina")
    instaledPower = models.IntegerField(null=False, help_text="Define a Tensão Instalada pelo Cliente")
    pressao = models.IntegerField(null=False, help_text="Define a Pressão Instalada pelo Cliente")

    def __str__(self):
        return str(self.numeroSerie)