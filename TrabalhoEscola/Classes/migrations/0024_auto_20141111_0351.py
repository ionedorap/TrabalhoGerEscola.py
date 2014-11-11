# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0023_auto_20141111_0336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='cursoNome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='cursoTurno',
            new_name='Turno',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='disciplinaDescricao',
            new_name='Descricao',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='disciplinaNome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='estrutura',
            old_name='estruturaAno',
            new_name='Ano',
        ),
        migrations.RenameField(
            model_name='estrutura',
            old_name='estruturaCurso',
            new_name='Curso',
        ),
        migrations.RenameField(
            model_name='estruturadisciplinaperiodo',
            old_name='estdiscperDisciplina',
            new_name='Disciplina',
        ),
        migrations.RenameField(
            model_name='estruturadisciplinaperiodo',
            old_name='estdiscperEstrutura',
            new_name='Estrutura',
        ),
        migrations.RenameField(
            model_name='estruturadisciplinaperiodo',
            old_name='estdiscperPeriodo',
            new_name='Periodo',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='periodoDescricao',
            new_name='Descricao',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='periodoIdentificacao',
            new_name='Identificacao',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='periodoPeriodo',
            new_name='Periodo',
        ),
        migrations.RenameField(
            model_name='semestre',
            old_name='semestreAno',
            new_name='Ano',
        ),
        migrations.RenameField(
            model_name='semestre',
            old_name='semestreSemestre',
            new_name='Semestre',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='turmaDescricao',
            new_name='Descricao',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='turmaEstrutura',
            new_name='Estrutura',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='turmaNome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='turmaSemestre',
            new_name='Semestre',
        ),
        migrations.RenameField(
            model_name='turmadisciplina',
            old_name='turmadiscDisciplina',
            new_name='Disciplina',
        ),
        migrations.RenameField(
            model_name='turmadisciplina',
            old_name='turmadiscEstruturaDisciplina',
            new_name='EstruturaDisciplina',
        ),
        migrations.RenameField(
            model_name='turmadisciplina',
            old_name='turmadiscTurma',
            new_name='Turma',
        ),
    ]
