# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alunoNome', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Aluno')),
                ('alunoSexo', models.CharField(max_length=10, null=True, verbose_name=b'Sexo', choices=[(b'Masculino', b'Masculino'), (b'Feminino', b'Feminino')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cursoNome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplinaNome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('disciplinaDescricao', models.CharField(max_length=100, null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o da Disciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estruturaAno', models.DateField(null=True, verbose_name=b'Ano de Cria\xc3\xa7\xc3\xa3o')),
                ('estruturaCurso', models.ForeignKey(verbose_name=b'Curso', to='Classes.Curso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstruturaDisciplinaPeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estdiscperDisciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Classes.Disciplina', null=True)),
                ('estdiscperEstrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Classes.Estrutura', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horarioTime', models.TimeField(null=True, verbose_name=b'Data Fim da inscricao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodoNome', models.CharField(max_length=100, null=True, verbose_name=b'Per\xc3\xadodo')),
                ('periododescricao', models.CharField(max_length=100, null=True, verbose_name=b'descri\xc3\xa7\xc3\xa3o do Per\xc3\xadodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('professorNome', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Professor')),
                ('professorFormacao', models.CharField(max_length=100, null=True, verbose_name=b'Forma\xc3\xa7\xc3\xa3o')),
                ('professorSexo', models.CharField(max_length=10, null=True, verbose_name=b'Sexo', choices=[(b'Masculino', b'Masculino'), (b'Feminino', b'Feminino')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semestreNome', models.CharField(max_length=1, null=True, verbose_name=b'Escolha o Semestre', choices=[(b'1', b'1\xc2\xb0'), (b'2', b'2\xc2\xb0'), (b'3', b'3\xc2\xb0'), (b'4', b'4\xc2\xb0'), (b'5', b'5\xc2\xb0'), (b'6', b'6\xc2\xb0'), (b'7', b'7\xc2\xb0'), (b'8', b'8\xc2\xb0'), (b'9', b'9\xc2\xb0'), (b'10', b'10\xc2\xb0'), (b'11', b'11\xc2\xb0'), (b'12', b'12\xc2\xb0'), (b'Depend\xc3\xaancia', b'Depend\xc3\xaancia')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turmaDescricao', models.CharField(max_length=100, null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o da Turma')),
                ('turmaEstrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Classes.Estrutura', null=True)),
                ('turmaSemestre', models.ForeignKey(verbose_name=b'Semestre', to='Classes.Semestre', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turmaalunoAluno', models.ForeignKey(verbose_name=b'Aluno', to='Classes.Aluno', null=True)),
                ('turmaalunoTurma', models.ForeignKey(verbose_name=b'Turma', to='Classes.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDiscHorProf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turmadischorprofHorario', models.ForeignKey(verbose_name=b'Horario', to='Classes.Horario', null=True)),
                ('turmadischorprofProfessor', models.ForeignKey(verbose_name=b'Professor', to='Classes.Professor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='estruturadisciplinaperiodo',
            name='estdiscperPeriodo',
            field=models.ForeignKey(verbose_name=b'Periodo', to='Classes.Periodo', null=True),
            preserve_default=True,
        ),
    ]
