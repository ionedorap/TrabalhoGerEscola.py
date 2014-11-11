# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0021_auto_20141111_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplinaaluno',
            old_name='disciplinaalunoDisciplina',
            new_name='Disciplina',
        ),
        migrations.RenameField(
            model_name='disciplinaaluno',
            old_name='disciplinaalunoTurmaAluno',
            new_name='TurmaAluno',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='ComecoTime',
            new_name='Comeco',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='FimTime',
            new_name='Fim',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='TurnoTime',
            new_name='Turno',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='professorFormacao',
            new_name='Formacao',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='professorNome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='professorSexo',
            new_name='Sexo',
        ),
    ]
