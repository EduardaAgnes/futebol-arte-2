# Generated by Django 5.0.2 on 2024-03-05 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_competicao_titulo_alter_clube_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clube',
            options={'verbose_name_plural': 'Clubes'},
        ),
        migrations.AlterModelOptions(
            name='titulo',
            options={'verbose_name_plural': 'Títulos'},
        ),
    ]