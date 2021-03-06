# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0002_auto_20141106_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodo',
            old_name='periododescricao',
            new_name='periodoDescricao',
        ),
        migrations.RemoveField(
            model_name='periodo',
            name='periodoNome',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='periodoPeriodo',
            field=models.CharField(max_length=2, null=True, verbose_name=b'Escolha o Periodo', choices=[(b'1', b'1\xc2\xb0'), (b'2', b'2\xc2\xb0'), (b'3', b'3\xc2\xb0'), (b'4', b'4\xc2\xb0'), (b'5', b'5\xc2\xb0'), (b'6', b'6\xc2\xb0'), (b'7', b'7\xc2\xb0'), (b'8', b'8\xc2\xb0'), (b'9', b'9\xc2\xb0'), (b'10', b'10\xc2\xb0'), (b'11', b'11\xc2\xb0'), (b'12', b'12\xc2\xb0'), (b'Depend\xc3\xaancia', b'Depend\xc3\xaancia')]),
        ),
    ]
