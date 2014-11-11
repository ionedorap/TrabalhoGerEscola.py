# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0005_auto_20141111_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='horarioTime',
            new_name='FimTime',
        ),
        migrations.AddField(
            model_name='horario',
            name='ComecoTime',
            field=models.TimeField(null=True, verbose_name=b'In\xc3\xadcio da aula'),
            preserve_default=True,
        ),
    ]
