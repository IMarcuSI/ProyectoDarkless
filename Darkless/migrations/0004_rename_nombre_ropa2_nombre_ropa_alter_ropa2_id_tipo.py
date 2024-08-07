# Generated by Django 5.0.6 on 2024-06-28 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Darkless', '0003_ropa2_tipo_delete_ropa_ropa2_id_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa2',
            old_name='nombre',
            new_name='nombre_ropa',
        ),
        migrations.AlterField(
            model_name='ropa2',
            name='id_tipo',
            field=models.ForeignKey(db_column='IDTipo', on_delete=django.db.models.deletion.CASCADE, to='Darkless.tipo'),
        ),
    ]
