# Generated by Django 5.0.2 on 2024-02-26 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'api_sedes',
            },
        ),
        migrations.CreateModel(
            name='Ventanilla',
            fields=[
                ('id_ventanilla', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=5)),
                ('detalles', models.TextField(blank=True, null=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(default=1)),
                ('asistencia', models.CharField(default='PE', max_length=3)),
                ('id_abogado', models.IntegerField(blank=True, null=True)),
                ('fecha_conf_coordinador', models.DateTimeField(blank=True, null=True)),
                ('fecha_conf_abogado', models.DateTimeField(blank=True, null=True)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sede')),
            ],
            options={
                'db_table': 'api_ventanilla',
            },
        ),
    ]
