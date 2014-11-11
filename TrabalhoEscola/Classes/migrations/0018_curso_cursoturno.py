# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0017_remove_curso_cursoturno'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='cursoTurno',
            field=models.CharField(max_length=12, null=True, verbose_name=b'Escolha o Turno', choices=[(b'Matutino', b'Matutino'), (b'Vespertino', b'Vespertino'), (b'Noturno', b'Noturno')]),
            preserve_default=True,
        ),
    ]
