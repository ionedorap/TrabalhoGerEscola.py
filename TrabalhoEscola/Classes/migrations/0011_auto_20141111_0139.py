# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0010_auto_20141111_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turmadischorprof',
            old_name='turmadischorprofHorario',
            new_name='Horario',
        ),
        migrations.RenameField(
            model_name='turmadischorprof',
            old_name='turmadischorprofProfessor',
            new_name='Professor',
        ),
        migrations.RenameField(
            model_name='turmadischorprof',
            old_name='turmadischorprofTurmaDisciplina',
            new_name='Turma',
        ),
        migrations.AddField(
            model_name='turmadischorprof',
            name='Disciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='Classes.Disciplina', null=True),
            preserve_default=True,
        ),
    ]
