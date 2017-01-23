# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Materia',
            new_name='Estudiante',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='code',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='linenos',
            new_name='cedula',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='language',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='title',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='style',
            new_name='provincia',
        ),
    ]
