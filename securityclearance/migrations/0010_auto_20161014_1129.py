# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0009_apprequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='complexity',
            field=models.CharField(default=b'M', max_length=8, choices=[(b'Simple', b'Simple'), (b'Medium', b'Medium'), (b'Complex', b'Complex')]),
        ),
    ]
