# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0008_auto_20141111_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='turmaNome',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Nome', choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='turma',
            name='turmaDescricao',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Descricao'),
        ),
    ]
