# Generated by Django 4.2.1 on 2023-07-06 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_producto_rename_apellido_formulario_nombrecompleto_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Formulario',
        ),
    ]
