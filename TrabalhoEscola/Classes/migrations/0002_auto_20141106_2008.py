# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplinaalunoTurma', models.ForeignKey(verbose_name=b'Turma', to='Classes.Turma')),
                ('disciplinaalunoTurmaAluno', models.ForeignKey(verbose_name=b'Turma Aluno', to='Classes.TurmaAluno', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='semestre',
            name='semestreNome',
        ),
        migrations.AddField(
            model_name='periodo',
            name='periodoPeriodo',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Escolha o Periodo', choices=[(b'1', b'1\xc2\xb0'), (b'2', b'2\xc2\xb0'), (b'3', b'3\xc2\xb0'), (b'4', b'4\xc2\xb0'), (b'5', b'5\xc2\xb0'), (b'6', b'6\xc2\xb0'), (b'7', b'7\xc2\xb0'), (b'8', b'8\xc2\xb0'), (b'9', b'9\xc2\xb0'), (b'10', b'10\xc2\xb0'), (b'11', b'11\xc2\xb0'), (b'12', b'12\xc2\xb0'), (b'Depend\xc3\xaancia', b'Depend\xc3\xaancia')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semestre',
            name='semestreAno',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Ano'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='semestre',
            name='semestreSemestre',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Escolha o Semestre', choices=[(b'1', b'1'), (b'2', b'2')]),
            preserve_default=True,
        ),
    ]
