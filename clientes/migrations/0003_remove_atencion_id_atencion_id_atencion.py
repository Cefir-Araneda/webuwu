# Generated by Django 4.1.6 on 2023-06-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_mantencion_alter_mecanico_rut_atencion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencion',
            name='id',
        ),
        migrations.AddField(
            model_name='atencion',
            name='id_atencion',
            field=models.AutoField(db_column='idAtencion', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
