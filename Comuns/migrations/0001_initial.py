# Generated by Django 5.0.2 on 2024-03-05 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=80, null=True)),
            ],
            options={
                'verbose_name_plural': 'ESTADOS',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=80, null=True)),
            ],
            options={
                'verbose_name_plural': 'PAÍSES',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=80, null=True)),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Comuns.estado')),
            ],
            options={
                'verbose_name_plural': 'CIDADES',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Comuns.pais'),
        ),
    ]
