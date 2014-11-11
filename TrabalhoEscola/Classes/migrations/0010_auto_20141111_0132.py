# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0009_auto_20141111_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplinaaluno',
            name='disciplinaalunoTurma',
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='disciplinaalunoDisciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='Classes.Disciplina', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='turmadischorprof',
            name='turmadischorprofTurmaDisciplina',
            field=models.ForeignKey(verbose_name=b'Turma', to='Classes.Turma', null=True),
            preserve_default=True,
        ),
    ]
