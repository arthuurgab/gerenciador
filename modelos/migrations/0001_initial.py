# Generated by Django 4.2.14 on 2024-08-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
