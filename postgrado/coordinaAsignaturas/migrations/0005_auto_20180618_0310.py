# Generated by Django 2.0.4 on 2018-06-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinaAsignaturas', '0004_auto_20180610_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='inscripciones',
            field=models.ManyToManyField(blank=True, to='coordinaAsignaturas.Inscripcion'),
        ),
    ]