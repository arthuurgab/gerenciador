# Generated by Django 4.2.14 on 2024-08-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maquinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('apelido', models.CharField(help_text='Define o Apelido (Nome) do Equipamento', max_length=250)),
                ('numeroSerie', models.CharField(help_text='Define o Número de Série do Equipamento', max_length=10, unique=True)),
                ('altura', models.FloatField(help_text='Define a Altura do Equipamento', null=True)),
                ('largura', models.FloatField(help_text='Define a Largura do Equipamento', null=True)),
                ('comprimento', models.FloatField(help_text='Define o Comprimento do Equipamento', null=True)),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquinas.maquina')),
            ],
        ),
    ]
