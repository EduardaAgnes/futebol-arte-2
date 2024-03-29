# Generated by Django 5.0.2 on 2024-03-04 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clube_delete_futebolarte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clube',
            old_name='ano_fundacao',
            new_name='ano_de_fundacao',
        ),
        migrations.AddField(
            model_name='clube',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='clube',
            name='cidade',
            field=models.CharField(choices=[('SP', 'SÃO PAULO'), ('RJ', 'RIO DE JANEIRO'), ('PI', 'TERESINA')], max_length=120, null=True),
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('posicao', models.CharField(choices=[('ATC', 'ATACANTE'), ('DEF', 'ZAGUEIRO'), ('LAT', 'LATERAL')], max_length=100, null=True, verbose_name='POSIÇÃO')),
                ('numero_da_camisa', models.IntegerField(verbose_name='NÚMERO')),
                ('sexo', models.CharField(choices=[('F', 'FEMININO'), ('M', 'MASCULINO')], max_length=80, null=True)),
                ('clube', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.clube')),
            ],
            options={
                'verbose_name_plural': 'Jogadores',
            },
        ),
    ]
