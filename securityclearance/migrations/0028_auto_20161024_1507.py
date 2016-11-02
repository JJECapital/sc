# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityclearance', '0027_auto_20161024_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprequest',
            name='comments',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
    ]
