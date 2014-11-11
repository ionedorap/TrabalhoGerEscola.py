# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0003_auto_20141106_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horarioTime',
            field=models.TimeField(null=True, verbose_name=b'Come\xc3\xa7o e t\xc3\xa9rmino da aula'),
        ),
    ]
