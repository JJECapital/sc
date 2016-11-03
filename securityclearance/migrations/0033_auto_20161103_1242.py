# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0032_auto_20161031_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='comments',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
    ]
