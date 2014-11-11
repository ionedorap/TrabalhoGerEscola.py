# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0018_curso_cursoturno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='professorFormacao',
            field=models.TextField(),
        ),
    ]
