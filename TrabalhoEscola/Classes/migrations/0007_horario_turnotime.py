# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0006_auto_20141111_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='TurnoTime',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Turno'),
            preserve_default=True,
        ),
    ]
