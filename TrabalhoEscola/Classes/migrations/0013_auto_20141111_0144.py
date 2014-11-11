# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0012_auto_20141111_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='turmadischorprof',
            name='Horario',
            field=models.ForeignKey(verbose_name=b'Horario', to='Classes.Horario', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='turmadischorprof',
            name='Professor',
            field=models.ForeignKey(verbose_name=b'Professor', to='Classes.Professor', null=True),
            preserve_default=True,
        ),
    ]
