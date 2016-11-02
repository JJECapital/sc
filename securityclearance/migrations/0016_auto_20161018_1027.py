# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0015_auto_20161018_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='status',
            field=models.CharField(default=b'Submitted', max_length=16, choices=[(b'Submitted', b'Submitted'), (b'Packaging', b'Packaging'), (b'UAT', b'UAT'), (b'Completed', b'Completed')]),
        ),
    ]
