from django.db import models

class Maquina(models.Model):
    # Define o Status da Máquina
    status = (
        (0, 'Inativo'),
        (1, 'Ativo'),
    )

    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    apelido = models.CharField(max_length=250, blank=False, help_text="Define o Apelido (Nome) da Máquina")
    serie = models.IntegerField(unique=True, null=False, help_text="Define o Número de Série da Máquina")
    tipo = models.CharField(max_length=250, blank=False, help_text="Define o Tipo da Máquina")
    fabricante = models.CharField(max_length=250, blank=True, help_text="Define o Fabricante da Máquina")
    modelo = models.CharField(max_length=250, blank=False, help_text="Define o Fabricante da Máquina")
    status = models.IntegerField(choices=status, default=1, help_text="Define o Status da Máquina, por Padrão Ativa (1)")
    data = models.DateField(null=False, blank=False, help_text="Define o Data da Instalação da Máquina")
    custo = models.FloatField(null=False, blank=True, help_text="Define o Custo da Máquina")
    local = models.CharField(max_length=250, blank=True, help_text="Define onde a Máquina foi Instalda - Local/Setor")

    def __str__(self):
        return str(self.apelido)


class Especificacoes(models.Model):
    # Define as Voltagens Comuns
    volts = (
        (110, '110V'),
        (220, '220V'),
        (240, '240V'),
        (380, '380V'),
        (415, '415V'),
        (440, '440V'),
        (480, '480V'),
        (600, '600V'),
    )

    # Define a Tipo de Controle
    controle = (
        (0, "Manual"),
        (1, "Automatico"),
        (2, "Hibrido"),
    )

    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    voltagem = models.IntegerField(choices=volts, help_text="Define a voltagem da Máquina")
    controle = models.IntegerField(choices=controle, default=1, help_text="Define o Tipo de Controle da Máquina")

    # Capacidade da Máquina
    peso = models.FloatField(null=False, blank=True, help_text="Define o Peso da Máquina")
    velocidade = models.IntegerField(null=False, blank=True, help_text="Define a Velocidade da Máquina")
    potencia = models.IntegerField(null=False, blank=True, help_text="Define a Potencia da Máquina")

    # Dimensões da Máquina
    altura = models.FloatField(null=False, blank=True, help_text="Define o Peso da Máquina")
    largura = models.FloatField(null=False, blank=True, help_text="Define a Velocidade da Máquina")
    profundidade = models.FloatField(null=False, blank=True, help_text="Define a Potencia da Máquina")

    def __str__(self):
        return str(self.maquina)