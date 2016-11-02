# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0021_auto_20161020_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='assigned',
            field=models.CharField(default=b'Not Assigned', max_length=64),
        ),
    ]
