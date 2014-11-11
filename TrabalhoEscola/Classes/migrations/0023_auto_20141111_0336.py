# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0022_auto_20141111_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='alunoNome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='alunoSexo',
            new_name='Sexo',
        ),
        migrations.RenameField(
            model_name='turmaaluno',
            old_name='turmaalunoAluno',
            new_name='Aluno',
        ),
        migrations.RenameField(
            model_name='turmaaluno',
            old_name='turmaalunoTurma',
            new_name='Turma',
        ),
    ]
