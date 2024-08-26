from django.db import models
from maquinas.models import Maquina

class ManutencaoMaquina(models.Model):
    manutencao = (
        (0, 'Preventiva'),
        (1, 'Corretiva'),
    )

    YouN = (
        (0, 'Não'),
        (1, 'Sim'),
        (2, 'Sem Necessidade')
    )

    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    manutencao = models.IntegerField(choices=manutencao, null=False)
    dataManutencao = models.DateField(null=False, blank=False, help_text="Define o Data da Instalação da Máquina")
    descricao = models.CharField(max_length=250, null=False, help_text="Uma Breve Descrição do que foi Feito na Máquina")
    pecas = models.CharField(max_length=250, null=False, help_text="Define as Peças que Foram Trocadas na Máquina")
    horasParada = models.IntegerField(null=False, help_text="Define a Quantia de Tempo que a Máquina Ficou Parada")

    # CHECKLIST DE MÁQUINA
    # Lubrificações
    partesMoveis = models.IntegerField(choices=YouN, null=False, help_text="Lubrificar partes móveis conforme especificado no manual do fabricante.")
    niveisOleo = models.IntegerField(choices=YouN, null=False, help_text="Verificar os níveis de óleo e outros fluidos lubrificantes.")
    substituirOleo = models.IntegerField(choices=YouN, null=False, help_text="Substituir óleos ou lubrificantes que estejam contaminados ou vencidos.")

    # Filtros
    filtros = models.IntegerField(choices=YouN, null=False, help_text="Inspecionar e substituir filtros de ar, óleo e combustível.")

    # Componentes Eletricos
    conexoes = models.IntegerField(choices=YouN, null=False, help_text="Checar conexões elétricas e aterramento.")
    cabos = models.IntegerField(choices=YouN, null=False, help_text="Inspecionar cabos e conectores em busca de desgastes ou danos.")
    bateria = models.IntegerField(choices=YouN, null=False, help_text="Testar baterias e verificar os níveis de carga.")

    # Componentes Mecanicos
    componentes = models.IntegerField(choices=YouN, null=False, help_text="Inspecionar correias, engrenagens, rolamentos, eixos e outras partes móveis.")
    torque = models.IntegerField(choices=YouN, null=False, help_text="Verificar o torque dos parafusos e fixações.")
    transmissao = models.IntegerField(choices=YouN, null=False, help_text="Checar os sistemas de transmissão (correntes, polias, acoplamentos).")

    # Sensores
    sensores = models.IntegerField(choices=YouN, null=False, help_text="Testar sensores para garantir que estão funcionando corretamente.")
    atuadores = models.IntegerField(choices=YouN, null=False, help_text="Verificar atuadores e realizar calibrações necessárias.")

    # Funcionalidade
    ciclo = models.IntegerField(choices=YouN, null=False, help_text="Executar um ciclo de operação para verificar o funcionamento correto da máquina.")
    monitorar = models.IntegerField(choices=YouN, null=False, help_text="Monitorar vibrações e ruídos anormais.")
    checagem = models.IntegerField(choices=YouN, null=False, help_text="Checar os tempos de ciclo e eficiência operacional.")

    # Segurança
    seguranca = models.IntegerField(choices=YouN, null=False, help_text="Verificar todos os dispositivos de segurança (botões de parada de emergência, barreiras, sensores de segurança).")
    falhas = models.IntegerField(choices=YouN, null=False, help_text="Checar os sistemas de alarme e dispositivos de proteção contra falhas.")
    protecoes = models.IntegerField(choices=YouN, null=False, help_text="Garantir que todas as proteções e barreiras estejam no lugar e funcionando.")

    # Ferramentas de Manutenção
    ferramentasMecanicas = models.IntegerField(choices=YouN, null=False, help_text="Certificar-se de que todas as ferramentas de manutenção estão calibradas e em bom estado.")
    ferramentasEletricas = models.IntegerField(choices=YouN, null=False, help_text="Verificar se todos os equipamentos de medição e controle usados durante a manutenção estão funcionando corretamente.")

    def __str__(self):
        return str(f"{self.maquina} - {self.dataManutencao}")