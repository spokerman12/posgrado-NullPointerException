# Generated by Django 2.0.4 on 2018-06-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinaAsignaturas', '0002_auto_20180530_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='codAsig',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
    ]