# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0026_auto_20161024_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='phone',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
    ]
