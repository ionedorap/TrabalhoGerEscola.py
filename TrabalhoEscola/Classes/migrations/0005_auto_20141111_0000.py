# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0004_auto_20141110_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horarioTime',
            field=models.TimeField(null=True, verbose_name=b'T\xc3\xa9rmino da Aula'),
        ),
    ]
