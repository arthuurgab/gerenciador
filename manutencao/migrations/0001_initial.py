# Generated by Django 4.2.14 on 2024-08-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maquinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManutencaoMaquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('manutencao', models.IntegerField(choices=[(0, 'Preventiva'), (1, 'Corretiva')])),
                ('dataManutencao', models.DateField(help_text='Define o Data da Instalação da Máquina')),
                ('descricao', models.CharField(help_text='Uma Breve Descrição do que foi Feito na Máquina', max_length=250)),
                ('pecas', models.CharField(help_text='Define as Peças que Foram Trocadas na Máquina', max_length=250)),
                ('horasParada', models.IntegerField(help_text='Define a Quantia de Tempo que a Máquina Ficou Parada')),
                ('partesMoveis', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Lubrificar partes móveis conforme especificado no manual do fabricante.')),
                ('niveisOleo', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Verificar os níveis de óleo e outros fluidos lubrificantes.')),
                ('substituirOleo', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Substituir óleos ou lubrificantes que estejam contaminados ou vencidos.')),
                ('filtros', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Inspecionar e substituir filtros de ar, óleo e combustível.')),
                ('conexoes', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Checar conexões elétricas e aterramento.')),
                ('cabos', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Inspecionar cabos e conectores em busca de desgastes ou danos.')),
                ('bateria', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Testar baterias e verificar os níveis de carga.')),
                ('componentes', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Inspecionar correias, engrenagens, rolamentos, eixos e outras partes móveis.')),
                ('torque', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Verificar o torque dos parafusos e fixações.')),
                ('transmissao', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Checar os sistemas de transmissão (correntes, polias, acoplamentos).')),
                ('sensores', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Testar sensores para garantir que estão funcionando corretamente.')),
                ('atuadores', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Verificar atuadores e realizar calibrações necessárias.')),
                ('ciclo', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Executar um ciclo de operação para verificar o funcionamento correto da máquina.')),
                ('monitorar', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Monitorar vibrações e ruídos anormais.')),
                ('checagem', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Checar os tempos de ciclo e eficiência operacional.')),
                ('seguranca', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Verificar todos os dispositivos de segurança (botões de parada de emergência, barreiras, sensores de segurança).')),
                ('falhas', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Checar os sistemas de alarme e dispositivos de proteção contra falhas.')),
                ('protecoes', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Garantir que todas as proteções e barreiras estejam no lugar e funcionando.')),
                ('ferramentasMecanicas', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Certificar-se de que todas as ferramentas de manutenção estão calibradas e em bom estado.')),
                ('ferramentasEletricas', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Sem Necessidade')], help_text='Verificar se todos os equipamentos de medição e controle usados durante a manutenção estão funcionando corretamente.')),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquinas.maquina')),
            ],
        ),
    ]
