# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0019_auto_20141111_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='professorFormacao',
            field=models.TextField(verbose_name=b'Forma\xc3\xa7\xc3\xa3o do Professor'),
        ),
    ]
