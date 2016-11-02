# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0018_auto_20161020_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprequest',
            name='customer',
            field=models.CharField(default='DimensionData', max_length=32),
            preserve_default=False,
        ),
    ]
