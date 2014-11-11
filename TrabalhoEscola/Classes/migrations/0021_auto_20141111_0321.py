# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0020_auto_20141111_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='periodoIdentificacao',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Identifica\xc3\xa7\xc3\xa3o ', choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='periodoDescricao',
            field=models.CharField(max_length=100, null=True, verbose_name=b'descri\xc3\xa7\xc3\xa3o do Per\xc3\xadodo '),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='periodoPeriodo',
            field=models.CharField(max_length=2, null=True, verbose_name=b'Escolha o Periodoc', choices=[(b'1', b'1\xc2\xb0'), (b'2', b'2\xc2\xb0'), (b'3', b'3\xc2\xb0'), (b'4', b'4\xc2\xb0'), (b'5', b'5\xc2\xb0'), (b'6', b'6\xc2\xb0'), (b'7', b'7\xc2\xb0'), (b'8', b'8\xc2\xb0'), (b'9', b'9\xc2\xb0'), (b'10', b'10\xc2\xb0'), (b'11', b'11\xc2\xb0'), (b'12', b'12\xc2\xb0'), (b'Depend\xc3\xaancia', b'Depend\xc3\xaancia')]),
        ),
    ]
