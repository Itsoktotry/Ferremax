# Generated by Django 4.2.1 on 2023-07-11 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0007_producto_categorias_producto_diagnostico_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categorias',
            new_name='categoria',
        ),
    ]