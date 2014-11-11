# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0016_auto_20141111_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='cursoTurno',
        ),
    ]
