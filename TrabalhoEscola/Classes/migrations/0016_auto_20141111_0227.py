# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0015_auto_20141111_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaDisciplina_X_HorarioProfessor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Classes.Disciplina', null=True)),
                ('Horario', models.ForeignKey(verbose_name=b'Horario', to='Classes.Horario', null=True)),
                ('Professor', models.ForeignKey(verbose_name=b'Professor', to='Classes.Professor', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Classes.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='turmadischorprof',
            name='Disciplina',
        ),
        migrations.RemoveField(
            model_name='turmadischorprof',
            name='Horario',
        ),
        migrations.RemoveField(
            model_name='turmadischorprof',
            name='Professor',
        ),
        migrations.RemoveField(
            model_name='turmadischorprof',
            name='Turma',
        ),
        migrations.DeleteModel(
            name='TurmaDiscHorProf',
        ),
    ]
