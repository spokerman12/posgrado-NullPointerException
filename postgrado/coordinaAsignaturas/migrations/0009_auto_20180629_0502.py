# Generated by Django 2.0.5 on 2018-06-29 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinaAsignaturas', '0008_auto_20180629_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='anio',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1970)]),
        ),
    ]
