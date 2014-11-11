# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0014_auto_20141111_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turmadiscDisciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Classes.Disciplina', null=True)),
                ('turmadiscEstruturaDisciplina', models.ForeignKey(verbose_name=b'Estrutura Disciplina Per\xc3\xadodo', to='Classes.EstruturaDisciplinaPeriodo', null=True)),
                ('turmadiscTurma', models.ForeignKey(verbose_name=b'Turma', to='Classes.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='turmacurso',
            name='turmadiscCurso',
        ),
        migrations.RemoveField(
            model_name='turmacurso',
            name='turmadiscTurma',
        ),
        migrations.DeleteModel(
            name='TurmaCurso',
        ),
    ]
