# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0013_auto_20141111_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turmadiscCurso', models.ForeignKey(verbose_name=b'Curso', to='Classes.Curso', null=True)),
                ('turmadiscTurma', models.ForeignKey(verbose_name=b'Turma', to='Classes.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='turmadiscDisciplina',
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='turmadiscEstruturaDisciplina',
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='turmadiscTurma',
        ),
        migrations.DeleteModel(
            name='TurmaDisciplina',
        ),
    ]
