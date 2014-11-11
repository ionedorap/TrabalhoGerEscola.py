# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0011_auto_20141111_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turmadischorprof',
            name='Horario',
        ),
        migrations.RemoveField(
            model_name='turmadischorprof',
            name='Professor',
        ),
    ]
