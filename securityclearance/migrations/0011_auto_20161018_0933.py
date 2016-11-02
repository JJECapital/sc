# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0010_auto_20161014_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='priority',
            field=models.CharField(default=b'Low', max_length=8, choices=[(b'Simple', b'Simple'), (b'Medium', b'Medium'), (b'Complex', b'Complex')]),
        ),
        migrations.AlterField(
            model_name='apprequest',
            name='complexity',
            field=models.CharField(default=b'Medium', max_length=8, choices=[(b'Simple', b'Simple'), (b'Medium', b'Medium'), (b'Complex', b'Complex')]),
        ),
    ]
