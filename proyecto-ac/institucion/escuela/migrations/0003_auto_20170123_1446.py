# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_auto_20170123_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cedula',
            field=models.CharField(max_length=11, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ciudad',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='provincia',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
