# Generated by Django 5.0.2 on 2024-03-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('ano_fundacao', models.PositiveIntegerField(default=0)),
                ('divisao', models.CharField(blank=True, choices=[('A', '1º DIVISÃO'), ('B', '2ª DIVISÃO'), ('C', '3º DIVISÃO'), ('D', '4º DIVISÃO')], max_length=100)),
                ('cidade', models.CharField(choices=[('SP', 'SÃO PAULO'), ('RJ', 'RIO DE JANEIRO'), ('THE', 'PIAUÍ')], max_length=120, null=True)),
                ('estado', models.CharField(choices=[('SP', 'SÃO PAULO'), ('RJ', 'RIO DE JANEIRO'), ('PI', 'PIAUÍ')], max_length=120, null=True)),
                ('pais', models.CharField(choices=[('BRA', 'BRASIL'), ('EUA', 'ESTADOS UNIDOS')], max_length=120, null=True)),
                ('modalidade', models.CharField(blank=True, choices=[('F', 'FEMININA'), ('M', 'MASCULINA')], max_length=90)),
                ('cores', models.CharField(blank=True, max_length=80, null=True)),
                ('tem_mundial', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='futebolarte',
        ),
    ]
