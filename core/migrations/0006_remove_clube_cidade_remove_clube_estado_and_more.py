# Generated by Django 5.0.2 on 2024-03-05 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_clube_options_alter_titulo_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clube',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='clube',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='clube',
            name='pais',
        ),
    ]
