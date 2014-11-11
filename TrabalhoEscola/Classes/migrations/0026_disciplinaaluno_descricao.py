# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0025_auto_20141111_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplinaaluno',
            name='Descricao',
            field=models.TextField(null=True, verbose_name=b'Descricao'),
            preserve_default=True,
        ),
    ]
