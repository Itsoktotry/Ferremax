# Generated by Django 4.2 on 2024-05-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0011_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
